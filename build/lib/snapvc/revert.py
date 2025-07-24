import os
import pickle
from .snapshot import update_working_version
from .staging import data_json_load

def revert_to_snapshot(directory :str, house :str, version :str) -> None:
  housing_path = os.path.join(directory, house)
  root_path = os.path.join(housing_path, 'snapshot')
  json_path = os.path.join(housing_path, 'data.json')
  json_data :dict = data_json_load(json_path)
  version_int = int(version)
  if int(version) not in json_data['all_versions']:
    print('Snapshot does not exist.')
    return
  if int(version) == json_data['current_version']:
    print(f"Already at {version}")
    return
  for file in json_data:
    if file == 'current_version':
      update_working_version(housing_path, version_int)
      continue
    elif file == 'all_versions':
      continue
    elif json_data[file]["added_in"] > version_int or json_data[file]["deleted_in"] < version_int and json_data[file]["deleted_in"] != 0:
      delete_files(file)
    else:
      file_hash = ""
      if json_data[file]["all_hashes"].__contains__(version):
        file_hash = json_data[file]["all_hashes"][version]
      else:
        list_data: dict = json_data[file]["all_hashes"]
        available_versions = map(int, list(list_data.keys()))
        available_versions = list(available_versions)
        for available in reversed(available_versions):
          if available < version_int:
            file_hash = list_data[f'{available}']
            break
      add_files(file, root_path, file_hash)
  print(f'Reverted to snapshot {version}')

def delete_files(file_path :str) -> None:
  if os.path.exists(file_path):
    os.remove(file_path)
    print(f'Removed files: {file_path}')

def add_files(file_path :str, snapshot_path :str ,file_hash :str) -> None:
  file_version = os.path.join(snapshot_path, file_hash)
  with open(file_version, 'rb') as file_content:
    content = pickle.load(file_content)
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)
  with open(file_path, 'wb') as f:
    f.write(content)