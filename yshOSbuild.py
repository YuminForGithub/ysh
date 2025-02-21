code = """\
import os

def ysh_run():
    os.system("ysh_run")

# Add the function to the os module
os.run_ysh = ysh_run
"""

print("write/creating the code...")

# Create (or overwrite) the file named 'sitecustomize.py'
with open("sitecustomize.py", "w") as file:
  file.write(code)

print("sitecustomize.py has been created successfully!")
