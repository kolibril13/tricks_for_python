import os
fileNames_txt = [fileName for fileName in os.listdir("tex/") if fileName.endswith(".tex")]
print(fileNames_txt)

trigger = "PANDAS"
fileNames = [fileName for fileName in os.listdir()
             if fileName.startswith(trigger)]
print(fileNames)

