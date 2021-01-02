import os, zipfile, subprocess
from pathlib import Path

path = Path.home() / "Downloads"
dir_name = str(path) + "/"
extension = ".zip"
file_to_delete = 'dateiliste.csv'
os.chdir(dir_name)  # change directory from working dir to dir with files

for item in os.listdir(dir_name):  # loop through items in dir
    if item.endswith(extension):  # check for ".zip" extension
        item_name=item[:-4]
        file_name = os.path.abspath(item)  # get full path of files
        zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
        zip_ref.extractall(dir_name + item_name)  # extract file to dir
        print(os.listdir(dir_name + item_name + '/'))
        if file_to_delete in os.listdir(dir_name + item_name + '/'):  # deletes 'dateiliste.csv'
            os.remove(dir_name + item_name + '/' + file_to_delete)
        zip_ref.close()  # close file
        os.remove(file_name)  # delete zipped file
        subprocess.Popen(['xdg-open', dir_name + item_name + '/'])
