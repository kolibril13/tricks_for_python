import os
if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    module_name = os.path.basename(__file__)
    print(abspath)
    print(module_name)
    names= os.path.split(__file__)
    print( names[1].split(".") )