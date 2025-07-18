import os
import pickle
import ignore

dir_ignore = ignore.dir_ignore
files_ignore = ignore.files_ignore

def revert_to_snapshot(hash_digest):
  snapshot_path = f'.svcs_storage/snapshot/{hash_digest}'
  if os.path.exists(snapshot_path):
    with open(snapshot_path, 'rb') as f:
      snapshot_data = pickle.load(f)

    for file_path, content in snapshot_data['files'].items():
      os.makedirs(os.path.dirname(file_path), exist_ok=True)
      with open(file_path, 'wb') as f:
        f.write(content)

    current_files = set()
    for root, dirs, files in os.walk('..', topdown=True):
      dirs[:] = [d for d in dirs if d not in dir_ignore]
      if '.svcs_storage' in root:
        continue
      for file in files:
        if file in files_ignore:
          continue
        current_files.add(os.path.join(root, file))

    snapshot_files = set(snapshot_data['file_list'])
    print(snapshot_files)
    files_to_delete = current_files - snapshot_files

    for file_path in files_to_delete:
      os.remove(file_path)
      print(f'Remove {file_path}')

    print(f'Reverted to snapshot {hash_digest}')
  else:
    print('Snapshot does not exist.')