from .snapshot import SNAPSHOT
from .utils import current_version, working_version
from .staging import STAGING
from .revert import REVERT
from .housing import HOUSE
import os
import sys

directory = '.svcs'
house = ''
housing = HOUSE(directory)
current_directory = os.getcwd()

def init_svcs() -> None:
  global house
  if not svcs_initialized():
    os.makedirs(directory, exist_ok=True)
    house = 'main'
    housing.new_house(house)
    print(f'SVCS initialized\n Current house: {house}')
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

  house = housing.current_house()
  housing_path = os.path.join(directory, house)
  if command[1] == 'house':
    if command_length < 3:
      print(f'You are at {house}')
      return

    if command[2] == 'new':
      if command_length > 3:
        statement = housing.new_house(command[3])
        print(statement)
      else:
        print("Please define house name")
    elif command[2] == 'show':
      print(f"You have houses at\n {housing.all_house()}")
    else:
      statement = housing.move_house(command[2])
      print(statement)
  elif command[1] == 'ready':
    staging = STAGING(current_directory, directory, house)
    staging.ready()
  elif command[1] == 'snapshot':
    commiting = SNAPSHOT(current_directory, directory, house)
    commiting.snapshot()
  elif command[1] == 'revert':
    if command_length > 2:
      REVERT(directory, house, command[2]).soft_revert()
    else:
      print("Please define the version")
  elif command[1] == 'current':
    print(f'You are at version {working_version(housing_path)}')
  elif command[1] == 'snaps':
    print(f'There are {current_version(housing_path)} snaps')
  else:
    print('Unknown command!')
    print(help_command())

if __name__ == "__main__":
  main()