from pathlib import Path
path = Path.cwd().glob("n2*")
new_paths= [Path(x) for x in list(path)]
print(new_paths)
print(new_paths[0])