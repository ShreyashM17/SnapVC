import os
from .revert import REVERT
from .utils import working_version, data_json_dump

class HOUSE:
  def __init__(self, svcs_directory :str) -> None:
    self.house_name :str = ''
    self.working_location: str = ''
    self.svcs_directory :str = svcs_directory
    self.house_file :str = os.path.join(svcs_directory, "house.txt")
    self.all_house_file :str = os.path.join(svcs_directory, "all_house.txt")

  def new_house(self, house_name) -> str:
    self.house_name: str = house_name
    self.working_location = os.path.join(self.svcs_directory, house_name)
    if os.path.exists(self.working_location):
      return f'{house_name} already exists please choose other name'
    else:
      os.makedirs(self.working_location)
      self.generate_rooms()
      self.update_house(house_name)
      return f'You are at {house_name}'

  def generate_rooms(self) -> None:
    path = self.working_location
    snapshot = os.path.join(path, 'snapshot')
    ready = os.path.join(path, 'ready')
    data_file_path = os.path.join(path, "data.json")
    os.makedirs(snapshot)
    os.makedirs(ready)
    content = {"current_version": 0, "all_versions": []}
    data_json_dump(data_file_path, content)

  def current_house(self) -> str:
    try:
      house_file = os.path.join(self.svcs_directory, 'house.txt')
      house = open(house_file, 'r')
      current = house.read()
      house.close()
      return current
    except FileNotFoundError:
      print('File not found')
      return 'Point of no return'

  def update_house(self, house_name: str) -> None:
    self.update_current_house(house_name)
    with open(self.all_house_file, "a") as f:
      f.write(f"\n{house_name}")

  def update_current_house(self, house_name):
    self.house_name: str = house_name
    with open(self.house_file, "w") as f:
      f.write(house_name)

  def move_house(self, house_name: str) -> str:
    self.working_location = os.path.join(self.svcs_directory, house_name)
    if os.path.exists(self.working_location):
      self.update_current_house(house_name)
      version = working_version(self.working_location)
      REVERT(self.svcs_directory, self.house_name, version).hard_revert()
      return f'You are at {self.house_name}'
    else:
      return 'House does not exists'

  def all_house(self) -> str:
    house = open(self.all_house_file, 'r')
    all_houses = house.read().strip()
    house.close()
    return all_houses
