import os
import pickle
import ignore

dir_ignore = ignore.dir_ignore
files_ignore = ignore.files_ignore

def revert_to_snapshot(directory, house, version):
  version_path = f'{directory}/{house}/snapshot/{version}'
  if os.path.exists(version_path):
    version_files = os.listdir(version_path)
    hash_location = version_files[0]
    snapshot_path = f'{version_path}/{hash_location}'
    with open(snapshot_path, 'rb') as f:
      snapshot_data = pickle.load(f)

    for file_path, content in snapshot_data['files'].items():
      os.makedirs(os.path.dirname(file_path), exist_ok=True)
      with open(file_path, 'wb') as f:
        f.write(content)

    current_files = set()
    for root, dirs, files in os.walk('..', topdown=True):
      dirs[:] = [d for d in dirs if d not in dir_ignore]
      if 'svcs' in root:
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

    print(f'Reverted to snapshot {version}')
  else:
    print('Snapshot does not exist.')