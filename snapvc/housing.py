import os
from .revert import revert_to_snapshot
from .snapshot import working_version

def new_house(path :str, house_name :str) -> str:
  location = os.path.join(path, house_name)
  if os.path.exists(location):
    return 'Already exists please choose other name'
  else:
    os.makedirs(location)
    generate_rooms(location)
    update_house(path, house_name)
    return f'You are at {house_name}'

def generate_rooms(path :str) -> None:
  snapshot = os.path.join(path, 'snapshot')
  ready = os.path.join(path, 'ready')
  version = os.path.join(snapshot, "version.txt")
  current_version = os.path.join(snapshot, "current_version.txt")
  os.makedirs(snapshot)
  os.makedirs(ready)
  with open(version, "w") as f:
    f.write("0")
  with open(current_version, "w") as f:
    f.write("0")

def current_house(directory :str) -> str:
  try:
    house_file = os.path.join(directory, 'house.txt')
    house = open(house_file,'r')
    current = house.read()
    house.close()
    return current
  except FileNotFoundError:
    print('File not found')
    return 'Point of no return'

def update_house(path :str, house :str) -> None:
  house_file = os.path.join(path, "house.txt")
  all_house_file = os.path.join(path, "all_house.txt")
  with open(house_file, "w") as f:
    f.write(house)
  with open(all_house_file, "a") as f:
    f.write(f"\n{house}")

def move_house(current_directory :str, path :str, house :str) -> str:
  house_location = os.path.join(path, house)
  snapshot_dir = os.path.join(house_location, 'snapshot')
  if os.path.exists(house_location):
    update_house(path, house)
    version = working_version(snapshot_dir)
    revert_to_snapshot(current_directory, path, house, version)
    return f'You are at {house}'
  else:
    return 'House does not exists'

def all_house(path :str) -> str:
  all_house_file = os.path.join(path, 'all_house.txt')
  house = open(all_house_file, 'r')
  all_houses = house.read().strip()
  house.close()
  return all_houses
