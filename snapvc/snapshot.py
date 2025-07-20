import os
import hashlib
import pickle
import shutil

def if_directory_empty(directory) -> bool:
  if not os.path.isdir(directory):
    print(f"Error: '{directory}' is not a valid directory.")
    return False

  with os.scandir(directory) as it:
    return next(it, None) is None

def empty_ready_folder(directory) -> None:
  shutil.rmtree(directory)
  os.makedirs(directory)

def snapshot(current_directory, directory, current_house) -> None:
  working_directory = os.path.join(directory, current_house)
  ready_directory = os.path.join(working_directory, 'ready')
  snapshot_directory = os.path.join(working_directory, 'snapshot')
  if not if_directory_empty(ready_directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {'files': {}}

    for root, dirs, files in os.walk(ready_directory):
      for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, 'rb') as f:
          content = f.read()
          snapshot_hash.update(content)
          file_path = file_path.replace(ready_directory, current_directory)
          snapshot_data['files'][file_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data['file_list'] = list(snapshot_data['files'].keys())
    current_ver = current_version(snapshot_directory)
    hash_path = os.path.join(snapshot_directory, current_ver, hash_digest)
    if not os.path.exists(hash_path):
      save_at = os.path.join(snapshot_directory, str(update_version(snapshot_directory)))
      os.makedirs(save_at)
      save_file = os.path.join(save_at, hash_digest)
      with open(save_file, 'wb') as f:
        pickle.dump(snapshot_data, f)
      print(f'Snapshot created with hash {hash_digest}')
    else:
      print(f'Snapshot already exists')
    empty_ready_folder(ready_directory)
  else:
    print("Nothing to Snapshot")

def current_version(snapshot_directory) -> str:
  version_file_path = os.path.join(snapshot_directory, 'version.txt')
  version_file = open(version_file_path, 'r')
  version = version_file.read()
  version_file.close()
  return version

def update_version(snapshot_directory) -> int:
  version = current_version(snapshot_directory)
  version = int(version) + 1
  version_file_path = os.path.join(snapshot_directory, 'version.txt')
  version_file = open(version_file_path, 'w')
  version_file.write(f'{version}')
  version_file.close()
  update_working_version(snapshot_directory)
  return version

def working_version(snapshot_directory) -> str:
  current_version_file = os.path.join(snapshot_directory, 'current_version.txt')
  version_file = open(current_version_file, 'r')
  version = version_file.read()
  version_file.close()
  return version

def update_working_version(snapshot_directory, new_version = 0) -> str:
  if new_version != 0:
    version = new_version
  else:
    version = current_version(snapshot_directory)
  current_version_file = os.path.join(snapshot_directory, 'current_version.txt')
  version_file = open(current_version_file, 'w')
  version_file.write(f'{version}')
  version_file.close()
  return version