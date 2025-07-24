import os
from .ignore import dir_ignore, files_ignore
import shutil
from pathlib import Path
import hashlib
import json

def ready(current_dir :str, storage :str, house :str) -> None:
  directory = current_dir
  temp = os.path.join(storage, house, 'ready')
  json_file = os.path.join(storage, house, 'data.json')
  created_directory = set()
  with open(json_file, 'r') as data_file:
    hash_data :dict = json.load(data_file)
  for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in dir_ignore]
    for file in files:
      if file in files_ignore:
        continue

      file_path = os.path.join(root, file)
      if hash_data:
        if hash_data.get(file_path):
          hash_value = hashing(file_path)
          if hash_data[file_path]['updated_hash'] == hash_value:
            continue
      parent = Path(directory)
      child = Path(root)
      relative = child.relative_to(parent)
      folder = os.path.join(temp, str(relative))
      if relative not in created_directory:
        os.makedirs(folder, exist_ok=True)
        created_directory.add(relative)
      shutil.copy2(file_path, folder)

def hashing(file_path :str) -> str:
  hash_data = hashlib.sha256()
  with open(file_path, 'rb') as file:
    content = file.read()
  hash_data.update(content)
  return hash_data.hexdigest()

def data_json_load(file_path :str) -> dict:
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data

def data_json_dump(file_path :str, data) -> None:
  with open(file_path, 'w') as file:
    json.dump(data, file)