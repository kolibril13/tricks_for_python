from pathlib import Path

file_contents = [
    path.read_text()
    for path in Path.cwd().rglob('*.csv')
]
print(*file_contents, sep="\n")