from pathlib import Path
path = Path.cwd() /"files1" /"text1.csv"
text  = path.read_text()

print(text)