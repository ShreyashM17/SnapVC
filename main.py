from snapshot import snapshot, working_version, current_version
from staging import ready
from revert import revert_to_snapshot
from housing import new_house, current_house, move_house
import os
import sys

directory = 'svcs'
house = ''

def init_svcs():
  global house
  if not svcs_initialized():
    os.makedirs(directory, exist_ok=True)
    house = 'main'
    name = new_house(directory,house)
    print(f'SVCS initialized\n {name}')
    with open(f"{directory}/house.txt", "w") as f:
      f.write("main")
  else:
    print("Already initialized")

def svcs_initialized():
  return os.path.exists(directory)

def main():
  global house
  command = sys.argv
  command_length = len(command)
  if command[1] == 'init':
    init_svcs()
  elif svcs_initialized():
    house = current_house(directory)
    if command[1] == 'house':
      if command_length > 2:
        if command[2] == 'new':
          if command_length > 3:
            statement = new_house(directory, command[3])
            print(statement)
          else:
            print("Please define house name")
        else:
          statement = move_house(directory, command[2])
          print(statement)
      else:
        print(f'You are at {house}')
    elif command[1] == 'ready':
      ready(directory, house)
    elif command[1] == 'snapshot':
      snapshot(directory, house)
    elif command[1] == 'revert':
      revert_to_snapshot(directory, house, command[2])
    elif command[1] == 'current':
      print(f'You are at version {working_version(f'{directory}/{house}/snapshot')}')
    elif command[1] == 'snaps':
      print(f'There are {current_version(f'{directory}/{house}/snapshot')} snaps')
    else:
      print('Unknown command!')
  else:
    print("SVCS not initialized")

if __name__ == "__main__":
  main()