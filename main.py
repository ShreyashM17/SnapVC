from svcs import snapshot, revert_to_snapshot
import os

def init_svcs():
  os.makedirs('.svcs_storage', exist_ok=True)
  print('SVCS initialized')

if __name__ == '__main__':
  import sys
  command = sys.argv[1]

  if command == 'init':
    init_svcs()
  elif command == 'snapshot':
    snapshot('.')
  elif command == 'revert':
    revert_to_snapshot(sys.argv[2])
  else:
    print('Unknown command!')