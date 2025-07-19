import os

def new_house(path, house_name):
  location = f'{path}/{house_name}'
  if os.path.exists(location):
    return 'Already exists please choose other name'
  else:
    os.makedirs(location)
    generate_rooms(location)
    update_house(path, house_name)
    return f'You are at {house_name}'

def generate_rooms(path):
  snapshot = f'{path}/snapshot'
  ready = f'{path}/ready'
  version = f"{snapshot}/version.txt"
  current_version = f"{snapshot}/current_version.txt"
  os.makedirs(snapshot)
  os.makedirs(ready)
  with open(version, "w") as f:
    f.write("0")
  with open(current_version, "w") as f:
    f.write("0")

def current_house(directory):
  try:
    house = open(f'{directory}/house.txt','r')
    current = house.read()
    house.close()
    return current
  except:
    print("House not detected")

def update_house(path, house):
  with open(f"{path}/house.txt", "w") as f:
    f.write(house)

def move_house(path, house):
  if os.path.exists(f'{path}/{house}'):
    update_house(path, house)
    return f'You are at {house}'
  else:
    return 'House does not exists'