from pathlib import Path
path = Path.cwd() / 'new' /"hi"/"there"
path.mkdir(parents=True, exist_ok=False)

#If parents is true, any missing parents of this path are created as needed
#If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.

