import os, pickle, shutil
from .ignore import dir_ignore, files_ignore
from pathlib import Path
from .utils import data_json_load, hashing

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
  files_to_be_deleted(temp, existing_files_with_hashes, present_file_path)

def files_to_be_deleted(temp_path :str,existing_files_with_hashes :set, present_file_path :set) -> None:
  file_path = os.path.join(temp_path, 'to_be_deleted')
  if os.path.exists(file_path):
    os.remove(file_path)
  existing_files_with_hashes.remove("current_version")
  existing_files_with_hashes.remove("all_versions")
  set_of_files_to_be_deleted :set = existing_files_with_hashes - present_file_path
  if set_of_files_to_be_deleted:
    with open(file_path, 'wb') as data_file:
      pickle.dump(set_of_files_to_be_deleted, data_file)
