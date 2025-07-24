import os
import hashlib
import pickle
import shutil
from .utils import update_version, data_json_dump, data_json_load

def if_directory_empty(directory :str) -> bool:
  if not os.path.isdir(directory):
    print(f"Error: '{directory}' is not a valid directory.")
    return False

  with os.scandir(directory) as it:
    return next(it, None) is None

def empty_ready_folder(directory :str) -> None:
  shutil.rmtree(directory)
  os.makedirs(directory)

def snapshot(current_directory :str, directory :str, current_house :str) -> None:
  working_directory = os.path.join(directory, current_house)
  ready_directory = os.path.join(working_directory, 'ready')
  if not if_directory_empty(ready_directory):
    snapshot_directory = os.path.join(working_directory, 'snapshot')
    json_file = os.path.join(working_directory, 'data.json')
    current_ver: str = update_version(working_directory)
    hash_data :dict= data_json_load(json_file)
    for root, dirs, files in os.walk(ready_directory):
      for file in files:
        snapshot_hash = hashlib.sha256()
        file_path = os.path.join(root, file)

        with open(file_path, 'rb') as f:
          snapshot_data = f.read()
        snapshot_hash.update(snapshot_data)
        hash_digest = snapshot_hash.hexdigest()
        file_path = file_path.replace(ready_directory, current_directory)
        if hash_data.__contains__(file_path):
          if hash_data[file_path]["updated_hash"] == hash_digest:
            continue
          hash_data[file_path]["updated_hash"] = hash_digest
          hash_data[file_path]["all_hashes"][current_ver] = hash_digest
        else:
          data = dict({"added_in": 0, "deleted_in": 0, "updated_hash": "", "all_hashes": {}})
          data["added_in"] = int(current_ver)
          data["updated_hash"] = hash_digest
          data["all_hashes"][current_ver] = hash_digest
          hash_data[file_path] = data
        save_file = os.path.join(snapshot_directory, hash_digest)
        with open(save_file, 'wb') as snap_file:
          pickle.dump(snapshot_data, snap_file)
    data_json_dump(json_file, hash_data)
    print(f'Snapshot created')
    empty_ready_folder(ready_directory)
  else:
    print("Nothing to Snapshot")