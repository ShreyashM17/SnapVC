import os
import hashlib
import pickle
import ignore

svcs_ignore = ignore.ignore
dir_ignore = svcs_ignore['dirs']
files_ignore = svcs_ignore['files']

def snapshot(directory):
  snapshot_hash = hashlib.sha256()
  snapshot_data = {'files': {}}

  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue
      if '.svcs_storage' in os.path.join(root, file):
        continue

      file_path = os.path.join(root, file)

      with open(file_path, 'rb') as f:
        content = f.read()
        snapshot_hash.update(content)
        snapshot_data['files'][file_path] = content

  hash_digest = snapshot_hash.hexdigest()
  snapshot_data['file_list'] = list(snapshot_data['files'].keys())

  with open(f'.svcs_storage/{hash_digest}', 'wb') as f:
    pickle.dump(snapshot_data, f)

  print(f'Snapshot created with hash {hash_digest}')

def revert_to_snapshot(hash_digest):
  snapshot_path = f'.svcs_storage/{hash_digest}'
  if os.path.exists(snapshot_path):
    with open(snapshot_path, 'rb') as f:
      snapshot_data = pickle.load(f)

    for file_path, content in snapshot_data['files'].items():
      os.makedirs(os.path.dirname(file_path), exist_ok=True)
      with open(file_path, 'wb') as f:
        f.write(content)

    current_files = set()
    for root, dirs, files in os.walk('.', topdown=True):
      dirs[:] = [d for d in dirs if d not in svcs_ignore]
      if '.svcs_storage' in root:
        continue
      for file in files:
        current_files.add(os.path.join(root, file))

    snapshot_files = set(snapshot_data['file_list'])
    files_to_delete = current_files - snapshot_files

    for file_path in files_to_delete:
      os.remove(file_path)
      print(f'Remove {file_path}')

    print(f'Reverted to snapshot {hash_digest}')
  else:
    print('Snapshot does not exist.')