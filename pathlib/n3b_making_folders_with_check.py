from pathlib import Path

path = Path.cwd() / 'newx' / "hi" / "there"
if not path.is_dir():
    path.mkdir(parents=True, exist_ok=False)
    print("Folder was created")

# If parents is true, any missing parents of this path are created as needed
# If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.
