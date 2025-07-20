import os

def new_house(path, house_name) -> str:
  location = os.path.join(path, house_name)  # Cross-platform path
  if os.path.exists(location):
    return 'Already exists please choose other name'
  else:
    os.makedirs(location)
    generate_rooms(location)
    update_house(path, house_name)
    return f'You are at {house_name}'

def generate_rooms(path) -> None:
  snapshot = os.path.join(path, 'snapshot')  # Cross-platform path
  ready = os.path.join(path, 'ready')  # Cross-platform path
  version = os.path.join(snapshot, "version.txt")  # Cross-platform path
  current_version = os.path.join(snapshot, "current_version.txt")  # Cross-platform path
  os.makedirs(snapshot)
  os.makedirs(ready)
  with open(version, "w") as f:
    f.write("0")
  with open(current_version, "w") as f:
    f.write("0")

def current_house(directory) -> str:
  try:
    house_file = os.path.join(directory, 'house.txt')  # Cross-platform path
    house = open(house_file,'r')
    current = house.read()
    house.close()
    return current
  except FileNotFoundError:
    print('File not found')
    return 'Point of no return'

def update_house(path, house) -> None:
  house_file = os.path.join(path, "house.txt")  # Cross-platform path
  all_house_file = os.path.join(path, "all_house.txt")  # Cross-platform path
  with open(house_file, "w") as f:
    f.write(house)
  with open(all_house_file, "a") as f:
    f.write(f"\n{house}")

def move_house(path, house) -> str:
  house_location = os.path.join(path, house)  # Cross-platform path
  if os.path.exists(house_location):
    update_house(path, house)
    return f'You are at {house}'
  else:
    return 'House does not exists'

def all_house(path) -> str:
  all_house_file = os.path.join(path, 'all_house.txt')  # Cross-platform path
  house = open(all_house_file, 'r')
  all_houses = house.read().strip()
  house.close()
  return all_houses
