from snapshot import snapshot
from staging import ready
from revert import revert_to_snapshot
from housing import new_house, current_house
import os

directory = 'svcs'
house = ''

def init_svcs():
  global house
  if not svcs_not_initialized():
    os.makedirs(directory, exist_ok=True)
    house = 'main'
    new_house(directory,house)
    print('SVCS initialized you are at main')
    with open(f"{directory}/house.txt", "w") as f:
      f.write("main")
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
    house = current_house(directory)
    if command[1] == 'ready':
      ready(directory, house)
    elif command[1] == 'snapshot':
      snapshot(directory, house)
    elif command[1] == 'revert':
      revert_to_snapshot(directory, house, command[2])
    else:
      print('Unknown command!')
  else:
    print("SVCS not initialized")