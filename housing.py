import os

def new_house(house_name):
  os.makedirs(house_name)
  generate_rooms(house_name)

def generate_rooms(path):
  snapshot = f'{path}/snapshot'
  ready = f'{path}/ready'
  version = f"{snapshot}/version.txt"
  os.makedirs(snapshot)
  os.makedirs(ready)
  with open(version, "w") as f:
    f.write("1")

def current_house():
  try:
    from svcs import house
    return house.house
  except:
    print("SVCS not detected")