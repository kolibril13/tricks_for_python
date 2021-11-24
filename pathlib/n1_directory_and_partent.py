# basics
from pathlib import Path

path_to_file = Path(__file__).resolve()
BASE_DIR = Path(__file__).resolve().parent.parent
currentWorkingDirectory = Path(__file__).cwd()
home = Path.home()
downloads = Path.home() /"Downloads"

print(path_to_file)
print(BASE_DIR)
print(currentWorkingDirectory)
print(home)
print()