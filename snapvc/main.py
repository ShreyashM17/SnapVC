from .snapshot import snapshot, working_version, current_version
from .staging import ready
from .revert import revert_to_snapshot
from .housing import new_house, current_house, move_house, all_house
import os
import sys

directory = '.svcs'
house = ''
current_directory = os.getcwd()

def init_svcs() -> None:
  global house
  if not svcs_initialized():
    os.makedirs(directory, exist_ok=True)
    house = 'main'
    name = new_house(directory,house)
    print(f'SVCS initialized\n {name}')
    house_file = os.path.join(directory, "house.txt")
    all_house_file = os.path.join(directory, "all_house.txt")
    with open(house_file, "w") as f:
      f.write("main")
    with open(all_house_file, "w") as f:
      f.write("main")
  else:
    print("Already initialized")

def svcs_initialized() -> bool:
  return os.path.exists(directory)

def help_command() -> str:
  all_commands = '''
  List of all available commands
  - init  #To initialize svcs
  - house # View current house
  - house show #To view all the present houses
  - house <house-name> # Switch back to a house
  - house new <feature-branch>  # Create a new feature house
  - current # To get current version
  - snaps # To get total number of versions
  - ready # Stage your changes
  - snapshot # Create a snapshot
  - revert <version> # Revert to a version if needed
  '''
  return all_commands

def main() -> None:
  global house
  command = sys.argv
  command_length = len(command)
  if command_length < 2:
    print(help_command())
    return

  if command[1] == 'init':
    init_svcs()
    return

  if not svcs_initialized():
    print("SVCS not initialized please run \n svcs init")
    return

  house = current_house(directory)
  if command[1] == 'house':
    if command_length < 3:
      print(f'You are at {house}')
      return

    if command[2] == 'new':
      if command_length > 3:
        statement = new_house(directory, command[3])
        print(statement)
      else:
        print("Please define house name")
    elif command[2] == 'show':
      print(f"You have houses at\n {all_house(directory)}")
    else:
      statement = move_house(directory, command[2])
      print(statement)
  elif command[1] == 'ready':
    ready(current_directory, directory, house)
  elif command[1] == 'snapshot':
    snapshot(current_directory, directory, house)
  elif command[1] == 'revert':
    revert_to_snapshot(current_directory ,directory, house, command[2])
  elif command[1] == 'current':
    snapshot_path = os.path.join(directory, house, 'snapshot')
    print(f'You are at version {working_version(snapshot_path)}')
  elif command[1] == 'snaps':
    snapshot_path = os.path.join(directory, house, 'snapshot')
    print(f'There are {current_version(snapshot_path)} snaps')
  else:
    print('Unknown command!')
    print(help_command())

if __name__ == "__main__":
  main()