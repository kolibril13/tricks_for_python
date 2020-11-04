from pathlib import Path

example_dict = Path.cwd()/ "example"
all_py_files = example_dict.rglob('*.py')

text_to_search = "from manimlib.imports import *"
replacement_text = "from manim import *"

for py_file in all_py_files:
    text = py_file.read_text()
    text = text.replace(text_to_search, replacement_text)
    py_file.write_text(text)

print("Done!")