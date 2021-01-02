from pathlib import Path
import os

path_of_address = Path.home() / 'Documents/working_directory.txt'
working_directory = str(path_of_address.read_text()[:-1])
working_directory = "/home/jan-hendrik/projects/non_git"
command = f"""gnome-terminal --working-directory={working_directory} -e /opt/anaconda3/bin/jupyter-notebook"""
os.system(command)
