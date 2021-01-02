# Enter script code

###
import clipboard
clipboard.copy("abc")  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboard
##

##
keyboard.send_keys(output)
##

##
choices = ["something", "something else", "a third thing"]

retCode, choice = dialog.list_menu(choices)
if retCode == 0:
    keyboard.send_keys("You chose " + choice)
##

###
text = clipboard.get_selection()
keyboard.send_key("<delete>")
keyboard.send_keys("The text %s was here previously" % text)
###
import os
command = "gnome-screenshot -a  -f '/tmp/temp.png' "
os.system(command)