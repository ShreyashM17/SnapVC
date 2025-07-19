import os
import ignore
import shutil
from pathlib import Path

dir_ignore = ignore.dir_ignore
files_ignore = ignore.files_ignore

def ready(storage, house):
  directory = os.path.dirname(os.getcwd())
  temp = f'{storage}/{house}/ready'
  created_directory = set()
  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue

      file_path = f'{os.path.join(root, file)}'
      parent = Path(directory)
      child = Path(root)
      relative = child.relative_to(parent)
      folder = f'{temp}/{relative}'
      if relative not in created_directory:
        os.makedirs(folder, exist_ok=True)
        created_directory.add(relative)
      shutil.copy2(file_path, folder)