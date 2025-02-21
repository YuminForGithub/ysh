print("Importing modules...")
try:
  import tqdm, os, sys
  from colorama import Fore, Back, Style
except ModuleNotFoundError:
  print("Exception: Module not found. trying to installing modules...")
  try:
    import os
    os.system("pip install tqdm subprocess sys time colorama")
  except:
    print("Exception: (Any) of the module install was interrupted by the error.")
    exit(1)
except:
  print("Exception: Unknown error while installing module.")
  exit(1)

print("Functionalling setup starting...")

def color(prompt: str, color: str, style: str = ""):
  return f"{color + style}{prompt}{Style.RESET_ALL}"

if input(f"""
    {color("Welcome to YSH building package for python 3.12.4(or later)!", Fore.LIGHTGREEN_EX, Style.BRIGHT)}
    This will build the ysh aliases and install the ysh.
    To continue, Press return/enter to continue or any key to abort.
      """) != "":
  exit(0)

if input(f"""
  This will install:
    {color("~/yshrun.py\n    ~/ysh/yshrun.py\n  Functions\n   os.ysh_run(): run manually with os", Fore.MAGENTA, Style.BRIGHT)}
  And setup your command: `ysh_run` will be runned as:
    {color("`/usr/local/bin/python3.12 /usr/local/bin/ysh_run`", Fore.LIGHTGREEN_EX, Style.BRIGHT)}
  
  Build is stable at: Python 3.12.4 (64-bit build).
  This process may be unbuildable if you are running this program in unsupported version.
  
  This process will needed a git installation: by needed to do following steps:
    Clone: https://github.com/YuminForGithub/ysh.git
    Run following command: `git clone https://github.com/YuminForGithub/ysh.git`
  
  Please upgrade your git to very last released version, Or use the auto-update installation steps at the git.
  
  [This process is stable version of release at the version of 0.1 currently.]
  The needed fixed requirations will be responded at following e-mail: cuteyumin1004@gmail.com
  If you want to know more about this process deeper, please visit: https://github.com/YuminForGithub/ysh/ and see following file:
    README.md
  to know about what this does.
  If you still don't know what this do, leave the comment at the provided github repository's global homepage.
  Sys path is: {sys.path}
  
  To continue, Press return/enter to continue or any key to abort.
      """) != "":
  exit(0)

def installGit(processID: int):
  if processID == 1:
    os.system("cd ~ && git clone https://github.com/YuminForGithub/ysh.git")
  elif processID == 2:
    os.system("cp ~/ysh/yshrun.py ~/")
  elif processID == 3:
    os.system("chmod +x ~/yshrun.py && mv ~/yshrun.py \"/usr/local/bin/python3.12 /usr/local/bin/ysh_run\"")
  else:
    raise ValueError("Not valid proccess ID!")

for i in tqdm.tqdm(range(1, 3), desc="Building YSH"):
  installGit(i)

print("Building complete!")
if input("Do you want to continue to YSH immediately? (Return/Enter: YES or any key to NO): ") == "":
  os.system("ysh_run")
else:
  print("You can run ysh manually with: `ysh_run` command.")
  
