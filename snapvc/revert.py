import os
from .utils import data_json_load, data_json_dump, add_files, delete_files

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
      json_data['current_version'] = version_int
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
      json_data[file]["updated_hash"] = file_hash
  data_json_dump(json_path, json_data)
  print(f'Reverted to snapshot {version}')