import os, hashlib, pickle, shutil, gzip
from .utils import update_version, data_json_dump, data_json_load

class SNAPSHOT:
  def __init__(self, current_directory :str, directory :str, current_house :str) -> None:
    self.working_directory = os.path.join(directory, current_house)
    self.ready_directory = os.path.join(self.working_directory, 'ready')
    self.current_directory = current_directory
    self.snapshot_directory = os.path.join(self.working_directory, 'snapshot')
    self.json_file = os.path.join(self.working_directory, 'data.json')
    self._current_ver: None = None
    self._int_current_ver: None = None
    self._hash_data: None = None

  @property
  def current_ver(self):
    if self._current_ver is None:
      self._current_ver = update_version(self.working_directory)
    return self._current_ver

  @property
  def int_current_ver(self):
    if self._int_current_ver is None:
      self._int_current_ver = int(self.current_ver)
    return self._int_current_ver

  @property
  def hash_data(self):
    if self._hash_data is None:
      self._hash_data = data_json_load(self.json_file)
    return self._hash_data

  def if_directory_empty(self) -> bool:
    if not os.path.isdir(self.ready_directory):
      print(f"Error: '{self.ready_directory}' is not a valid directory.")
      return False

    with os.scandir(self.ready_directory) as it:
      return next(it, None) is None

  def files_deleted(self, file_path: str)-> None:
    with open(file_path, 'rb') as f:
      deleted: set = pickle.load(f)
    for file in deleted:
      self.hash_data[file]["deleted_in"] = self.int_current_ver

  @staticmethod
  def file_snapshot(file_path) -> (str, bytes):
    snapshot_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
      snapshot_data = f.read()
    snapshot_hash.update(snapshot_data)
    hash_digest = snapshot_hash.hexdigest()
    return hash_digest, snapshot_data

  def update_data_file(self, file_path, hash_digest):
    if self.hash_data.__contains__(file_path):
      self.hash_data[file_path]["updated_hash"] = hash_digest
      self.hash_data[file_path]["all_hashes"][self.current_ver] = hash_digest
    else:
      data = dict({"added_in": 0, "deleted_in": 0, "updated_hash": "", "all_hashes": {}})
      data["added_in"] = int(self.current_ver)
      data["updated_hash"] = hash_digest
      data["all_hashes"][self.current_ver] = hash_digest
      self.hash_data[file_path] = data

  def create_snapshot(self) -> None:
    for root, dirs, files in os.walk(self.ready_directory):
      for file in files:
        file_path = os.path.join(root, file)
        if file == 'to_be_deleted':
          self.files_deleted(file_path)
          continue
        hash_digest, snapshot_data = self.file_snapshot(file_path)
        file_path = file_path.replace(self.ready_directory, self.current_directory)
        self.update_data_file(file_path, hash_digest)
        save_file = os.path.join(self.snapshot_directory, hash_digest)
        with gzip.open(save_file, 'wb') as snap_file:
          pickle.dump(snapshot_data, snap_file)

  def empty_ready_folder(self) -> None:
    shutil.rmtree(self.ready_directory)
    os.makedirs(self.ready_directory)

  def snapshot(self) -> None:
    if not self.if_directory_empty():
      _ = self.current_ver
      _ = self.hash_data
      self.create_snapshot()
      data_json_dump(self.json_file, self.hash_data)
      print(f'Snapshot created')
      self.empty_ready_folder()
    else:
      print("Nothing to Snapshot")