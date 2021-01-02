from pathlib import Path
import os

path_of_address = Path.home() / 'Documents/working_directory.txt'
working_directory = path_of_address.read_text()
os.system("nautilus " + working_directory)
