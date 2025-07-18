from snapshot import snapshot
from staging import ready
from revert import revert_to_snapshot
import os

def init_svcs():
  os.makedirs('.svcs_storage', exist_ok=True)
  os.makedirs('.svcs_storage/ready', exist_ok=True)
  os.makedirs('.svcs_storage/snapshot', exist_ok=True)
  print('SVCS initialized')

def svcs_not_initialized():
  return os.path.exists('.svcs_storage')

if __name__ == '__main__':
  import sys
  command = sys.argv[1]

  if command == 'init':
    init_svcs()
  elif svcs_not_initialized():
    if command == 'ready':
      ready()
    elif command == 'snapshot':
      snapshot('.svcs_storage/ready')
    elif command == 'revert':
      revert_to_snapshot(sys.argv[2])
    else:
      print('Unknown command!')
  else:
    print("SVCS not initialized")