import os
from .ignore import dir_ignore, files_ignore
import shutil
from pathlib import Path

def ready(current_dir, storage, house):
  directory = current_dir
  temp = os.path.join(storage, house, 'ready')
  created_directory = set()
  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue

      file_path = os.path.join(root, file)
      parent = Path(directory)
      child = Path(root)
      relative = child.relative_to(parent)
      folder = os.path.join(temp, str(relative))
      if relative not in created_directory:
        os.makedirs(folder, exist_ok=True)
        created_directory.add(relative)
      shutil.copy2(file_path, folder)