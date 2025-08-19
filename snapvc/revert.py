import os
from .utils import data_json_load, data_json_dump, add_files, delete_files

class REVERT:
  def __init__(self, directory :str, house :str, version :str) -> None:
    self.housing_path = os.path.join(directory, house)
    self.root_path = os.path.join(self.housing_path, 'snapshot')
    self.json_path = os.path.join(self.housing_path, 'data.json')
    self.json_data: dict = data_json_load(self.json_path)
    self.version = version
    self.version_int = int(self.version)

  def revert(self) -> None:
    for file in self.json_data:
      if file == 'current_version':
        self.json_data['current_version'] = self.version_int
        continue
      elif file == 'all_versions':
        continue
      elif ((self.json_data[file]["added_in"] > self.version_int)
            or (self.json_data[file]["deleted_in"] < self.version_int)
            and (self.json_data[file]["deleted_in"] != 0)):
        delete_files(file)
      else:
        if self.json_data[file]["all_hashes"].__contains__(self.version):
          file_hash = self.json_data[file]["all_hashes"][self.version]
        else:
          file_hash = self.get_older_file_hash(file)
        add_files(file, self.root_path, file_hash)
        self.json_data[file]["updated_hash"] = file_hash
    data_json_dump(self.json_path, self.json_data)

  def get_older_file_hash(self, file) -> str:
    file_hash = ""
    list_data: dict = self.json_data[file]["all_hashes"]
    available_versions = list(map(int, list(list_data.keys())))
    for available in reversed(available_versions):
      if available < self.version_int:
        file_hash = list_data[f'{available}']
        break
    return file_hash

  def revert_checks(self) -> bool:
    if int(self.version) not in self.json_data['all_versions']:
      print('Snapshot does not exist.')
      return False
    if int(self.version) == self.json_data['current_version']:
      print(f"Already at {self.version}")
      return False
    return True

  def soft_revert(self) -> None:
    if self.revert_checks():
      self.revert()

  def hard_revert(self) -> None:
    self.revert()