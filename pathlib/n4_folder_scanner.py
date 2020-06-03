def Folderscanner():
    import glob, os
    # os.chdir("temp/")
    filenames = [img for img in glob.glob("/home/jan-hendrik/Desktop/test/*")]
    filenames.sort() # ADD THIS LINE
    return filenames

def FolderScanner2():
    from pathlib import Path
    prefix = "p"
    suffix = ".png"
    directory= Path.home() / "Desktop/test"
    file_names= [subp for subp in directory.rglob('*') if  (prefix in subp.name) & (suffix == subp.suffix)]
    file_names.sort()
    file_names_string  = [str(file_name) for file_name in file_names]
    return file_names_string

print(*Folderscanner(), sep="\n")
print(*FolderScanner2(), sep="\n")

