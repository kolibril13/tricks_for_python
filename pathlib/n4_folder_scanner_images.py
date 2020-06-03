from pathlib import Path


prefix = "dog"
suffix = ".jpg"
directory= Path.cwd() / "imgs"
file_names= [subp.name for subp in directory.rglob('*') if  (prefix in subp.name) & (suffix == subp.suffix)]
file_names.sort()
print(file_names)

print(Path(__file__).resolve())