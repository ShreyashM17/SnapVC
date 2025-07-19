import os
import pickle
import ignore
from snapshot import update_working_version

dir_ignore = ignore.dir_ignore
files_ignore = ignore.files_ignore

def revert_to_snapshot(directory, house, version):
  root_path = f'{directory}/{house}/snapshot'
  version_path = f'{root_path}/{version}'
  directory_list = os.listdir('..')
  if os.path.exists(version_path):
    version_files = os.listdir(version_path)
    hash_location = version_files[0]
    snapshot_path = f'{version_path}/{hash_location}'
    with open(snapshot_path, 'rb') as f:
      snapshot_data = pickle.load(f)
    created_directory = set()
    for file_path, content in snapshot_data['files'].items():
      directory_name = os.path.dirname(file_path)
      if directory_name not in directory_list:
        if directory_name not in created_directory:
          os.makedirs(directory_name, exist_ok=True)
          created_directory.add(directory_name)
      created_directory.add(directory_name)

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
    files_to_delete = current_files - snapshot_files
    removed_files = []
    if files_to_delete:
      for file_path in files_to_delete:
        os.remove(file_path)
        removed_files.append(file_path)
      print(f'Removed files: {removed_files}')
    update_working_version(root_path, version)
    print(f'Reverted to snapshot {version}')
  else:
    print('Snapshot does not exist.')