import os
import hashlib
import pickle
import shutil

def if_directory_empty(directory):
  if not os.path.isdir(directory):
    print(f"Error: '{directory}' is not a valid directory.")
    return False

  with os.scandir(directory) as it:
    return next(it, None) is None

def empty_ready_folder(directory):
  shutil.rmtree(directory)
  os.makedirs(directory)

def snapshot(directory, current_house):
  working_directory = f'{directory}/{current_house}'
  ready_directory = f'{working_directory}/ready'
  snapshot_directory = f'{working_directory}/snapshot'
  if not if_directory_empty(ready_directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {'files': {}}

    for root, dirs, files in os.walk(ready_directory):
      for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, 'rb') as f:
          content = f.read()
          snapshot_hash.update(content)
          file_path = file_path.replace(ready_directory,'..')
          snapshot_data['files'][file_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data['file_list'] = list(snapshot_data['files'].keys())

    save_at = f'{snapshot_directory}/{current_version(snapshot_directory)}'
    os.makedirs(save_at)
    with open(f'{save_at}/{hash_digest}', 'wb') as f:
      pickle.dump(snapshot_data, f)

    print(f'Snapshot created with hash {hash_digest}')
    update_version(snapshot_directory)
    empty_ready_folder(ready_directory)
  else:
    print("Nothing to Snapshot")

def current_version(snapshot_directory):
  version_file = open(f'{snapshot_directory}/version.txt', 'r')
  version = version_file.read()
  version_file.close()
  return version

def update_version(snapshot_directory):
  val = current_version(snapshot_directory)
  val = int(val) + 1
  version_file = open(f'{snapshot_directory}/version.txt', 'w')
  version_file.write(f'{val}')
  version_file.close()
