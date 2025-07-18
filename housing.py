import os
from svcs import house

def new_house(house_name):
  os.makedirs(house_name)
  generate_rooms(house_name)

def generate_rooms(path):
  snapshot = f'{path}/snapshot'
  ready = f'{path}/ready'
  version = f"{snapshot}/version.py"
  os.makedirs(snapshot)
  os.makedirs(ready)
  with open(version, "w") as f:
    f.write("version=1")

def current_house():
  print(f"You are at {house.house}")