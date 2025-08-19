import os, pickle, shutil
from .ignore import dir_ignore, files_ignore
from pathlib import Path
from .utils import data_json_load, hashing

class STAGING:
  def __init__(self, current_dir :str, storage :str, house :str) -> None:
    self.directory = current_dir
    self.house_path = os.path.join(storage, house)
    self.temp = os.path.join(self.house_path, 'ready')
    self.json_file = os.path.join(self.house_path, 'data.json')
    self.__created_directory = set()
    self.__present_file_path = set()
    self.hash_data: dict = data_json_load(self.json_file)
    self.existing_files_with_hashes = set(self.hash_data.keys())

  def copying_files(self):
    for root, dirs, files in os.walk(self.directory):
      dirs[:] = [d for d in dirs if d not in dir_ignore]
      for file in files:
        if file in files_ignore:
          continue
        file_path = os.path.join(root, file)
        self.__present_file_path.add(file_path)
        if self.check_hash_exists(file_path):
          continue
        parent = Path(self.directory)
        child = Path(root)
        relative = child.relative_to(parent)
        folder = os.path.join(self.temp, str(relative))
        if relative not in self.__created_directory:
          os.makedirs(folder, exist_ok=True)
          self.__created_directory.add(relative)
        shutil.copy2(file_path, folder)

  def check_hash_exists(self, file_path):
    if self.hash_data:
      if self.hash_data.get(file_path):
        hash_value = hashing(file_path)
        if self.hash_data[file_path]['updated_hash'] == hash_value:
          return True
    return False

  def files_to_be_deleted(self) -> None:
    file_path = os.path.join(self.temp, 'to_be_deleted')
    if os.path.exists(file_path):
      os.remove(file_path)
    self.existing_files_with_hashes.remove("current_version")
    self.existing_files_with_hashes.remove("all_versions")
    set_of_files_to_be_deleted: set = self.existing_files_with_hashes - self.__present_file_path
    if set_of_files_to_be_deleted:
      with open(file_path, 'wb') as data_file:
        pickle.dump(set_of_files_to_be_deleted, data_file)

  def ready(self) -> None:
    self.copying_files()
    self.files_to_be_deleted()