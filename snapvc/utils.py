import os, json, hashlib, pickle, gzip

def current_version(directory :str) -> str:
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r') as version_file:
    file_content = json.load(version_file)
    versions = file_content["all_versions"]
    if len(versions):
      version = file_content["all_versions"][-1]
    else:
      version = 0
  return version

def update_version(directory :str) -> str:
  version = current_version(directory)
  version = int(version) + 1
  version_file_path = os.path.join(directory, 'data.json')
  version_data = data_json_load(version_file_path)
  version_data["all_versions"].append(version)
  version_data["current_version"] = version
  data_json_dump(version_file_path, version_data)
  return str(version)

def working_version(directory :str) -> str:
  version_file_path = os.path.join(directory, 'data.json')
  with open(version_file_path, 'r') as version_file:
    file_content = json.load(version_file)
    version = file_content["current_version"]
  return version

def update_working_version(directory :str, new_version :int = 0) -> str:
  if new_version != 0:
    version = new_version
  else:
    version = current_version(directory)
  version_file_path = os.path.join(directory, 'data.json')
  current_version_saved = data_json_load(version_file_path)
  current_version_saved["current_version"] = version
  data_json_dump(version_file_path, current_version_saved)
  return version

def data_json_load(file_path :str) -> dict:
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data

def data_json_dump(file_path :str, data) -> None:
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)

def hashing(file_path :str) -> str:
  hash_data = hashlib.sha256()
  with open(file_path, 'rb') as file:
    content = file.read()
  hash_data.update(content)
  return hash_data.hexdigest()

def delete_files(file_path :str) -> None:
  if os.path.exists(file_path):
    os.remove(file_path)
    print(f'Removed files: {file_path}')

def add_files(file_path :str, snapshot_path :str ,file_hash :str) -> None:
  file_version = os.path.join(snapshot_path, file_hash)
  with gzip.open(file_version, 'rb') as file_content:
    content = pickle.load(file_content)
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)
  with open(file_path, 'wb') as f:
    f.write(content)