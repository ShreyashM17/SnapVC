import os
import hashlib
import pickle
import shutil
import json

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
    with open(json_file, 'r') as hash_data_file:
      hash_data :dict= json.load(hash_data_file)
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
          data = dict({"added_in": 0, "deleted_in": None, "updated_hash": "", "all_hashes": {}})
          data["added_in"] = int(current_ver)
          data["updated_hash"] = hash_digest
          data["all_hashes"][current_ver] = hash_digest
          hash_data[file_path] = data
        save_file = os.path.join(snapshot_directory, hash_digest)
        with open(json_file, 'w') as hash_data_file:
          json.dump(hash_data, hash_data_file, indent=2)
        with open(save_file, 'wb') as snap_file:
          pickle.dump(snapshot_data, snap_file)
        print(f'Snapshot created with hash {hash_digest}')
    empty_ready_folder(ready_directory)
  else:
    print("Nothing to Snapshot")

def current_version(directory :str) -> str:
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r') as version_file:
    file_content = json.load(version_file)
    versions = file_content["all_versions"]
    if len(versions):
      version = file_content["all_versions"][-1]
    else:
      version = 0
  return version

def update_version(directory :str) -> str:
  version = current_version(directory)
  version = int(version) + 1
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r+') as version_file:
    file_content = json.load(version_file)
    version_file.seek(0)
    version_file.truncate()
    file_content["all_versions"].append(version)
    file_content["current_version"] = version
    json.dump(file_content, version_file)
  return str(version)

def working_version(directory :str) -> str:
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r') as version_file:
    file_content = json.load(version_file)
    version = file_content["current_version"]
  return version

def update_working_version(directory :str, new_version :int = 0) -> str:
  if new_version != 0:
    version = new_version
  else:
    version = current_version(directory)
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r+') as version_file:
    file_content = json.load(version_file)
    version_file.seek(0)
    version_file.truncate()
    file_content["current_version"] = version
    json.dump(file_content, version_file)
  return version