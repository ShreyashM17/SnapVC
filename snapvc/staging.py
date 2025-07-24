import os
from .ignore import dir_ignore, files_ignore
import shutil
from pathlib import Path
from .utils import data_json_load, data_json_dump, hashing, current_version

def ready(current_dir :str, storage :str, house :str) -> None:
  directory = current_dir
  house_path = os.path.join(storage, house)
  temp = os.path.join(house_path, 'ready')
  json_file= os.path.join(house_path, 'data.json')
  created_directory = set()
  present_file_path = set()
  hash_data :dict = data_json_load(json_file)
  existing_files_with_hashes = set(hash_data.keys())
  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue

      file_path = os.path.join(root, file)
      present_file_path.add(file_path)
      if hash_data:
        if hash_data.get(file_path):
          hash_value = hashing(file_path)
          if hash_data[file_path]['updated_hash'] == hash_value:
            continue
      parent = Path(directory)
      child = Path(root)
      relative = child.relative_to(parent)
      folder = os.path.join(temp, str(relative))
      if relative not in created_directory:
        os.makedirs(folder, exist_ok=True)
        created_directory.add(relative)
      shutil.copy2(file_path, folder)
  check_files_to_delete(house_path, json_file, existing_files_with_hashes, present_file_path, hash_data)

def check_files_to_delete(house_path :str, json_path :str ,existing_files_with_hashes :set, present_file_path :set, hash_data :dict):
  existing_files_with_hashes.remove("current_version")
  existing_files_with_hashes.remove("all_versions")
  files_deleted = existing_files_with_hashes - present_file_path
  if files_deleted:
    for file in files_deleted:
      hash_data[file]["deleted_in"] = int(current_version(house_path)) + 1
    data_json_dump(json_path, hash_data)
