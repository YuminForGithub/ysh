import os
import getpass

user = getpass.getuser()
folder = os.path.basename(os.getcwd())
handlewith = 'sh'

print('PYKERNEL Running \nVersion 0.0.1 \nKernel with 3.12.4 (64-bit for mac)')
print(f'Logged in with {user} \n')
  
try:
  while True:
    command = input(f'{user}{f' > {folder} ' if folder != user and folder != '' else ''}{' > ' if folder == '' else ''}{'Grandfolder ' if folder == '' else ''}{' ' if folder == user else ''}| ')
    try:
      if command.startswith('cd '):
        try:
          # Extract the directory from the command and change to it
          directory = command[3:].strip()
          os.chdir(directory)
          folder = os.path.basename(os.getcwd())
        except Exception as e:
          print(f"Error: {e}")
      elif command == 'exit' or command == 'quit':
        exit(0)
      else:
        os.system(command)
    except Exception as e:
      print(f"Error: {e}")
except KeyboardInterrupt:
  print('''
  Ctrl+C/D: EOF - Exitted the kernel quickly...
  Aborting kernel...
  ''')
  exit(0)
