from snapshot import snapshot
from staging import ready
from revert import revert_to_snapshot
from housing import new_house
import os

directory = 'svcs'

def init_svcs():
  if not svcs_not_initialized():
    os.makedirs(directory, exist_ok=True)
    main = f'{directory}/main'
    new_house(main)
    print('SVCS initialized you are at main')
    with open(f"{directory}/house.py", "w") as f:
      f.write("house='main'")
  else:
    print("Already initialized")

def svcs_not_initialized():
  return os.path.exists(directory)

if __name__ == '__main__':
  import sys
  command = sys.argv

  if command[1] == 'init':
    init_svcs()
  elif svcs_not_initialized():
    if command[1] == 'ready':
      ready()
    elif command[1] == 'snapshot':
      snapshot('.svcs_storage/ready')
    elif command[1] == 'revert':
      revert_to_snapshot(command[2])
    else:
      print('Unknown command!')
  else:
    print("SVCS not initialized")