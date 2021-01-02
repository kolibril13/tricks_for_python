# requires:
# * sudo apt-get install gnome-screenshot
# * sudo apt-get install xclip 


import time
import os

working_directory = "~/Downloads/"

command = "gnome-screenshot -a  -f '/tmp/temp.png' "
os.system(command)

name = dialog.input_dialog(title='', message='Screenshot name:', default='').data

from_path = '/tmp/temp.png'
if name == "" :
    os.system("xclip -selection clipboard -t image/png -i /tmp/temp.png")
    
else:
    to_path = working_directory + name + '.png'
    command2 = "mv " + from_path + " " + to_path
    os.system(command2)
