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

def snapshot(directory):
  if not if_directory_empty(directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {'files': {}}

    for root, dirs, files in os.walk(directory):
      for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, 'rb') as f:
          content = f.read()
          snapshot_hash.update(content)
          file_path = file_path.replace(directory,'..')
          snapshot_data['files'][file_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data['file_list'] = list(snapshot_data['files'].keys())

    with open(f'.svcs_storage/snapshot/{hash_digest}', 'wb') as f:
      pickle.dump(snapshot_data, f)

    print(f'Snapshot created with hash {hash_digest}')
    empty_ready_folder(directory)
  else:
    print("Nothing to Snapshot")