import os
import ignore
import shutil

dir_ignore = ignore.dir_ignore
files_ignore = ignore.files_ignore

def ready(directory):
  temp = r'.svcs_storage/ready'
  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue
      if '.svcs_storage' in os.path.join(root, file):
        continue

      file_path = f'{os.path.join(root, file)}'
      shutil.copy(file_path, temp)