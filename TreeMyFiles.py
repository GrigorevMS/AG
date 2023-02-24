import os

def TreeFiles(startDir, tab):
    print("    " * tab, startDir[startDir.rfind("\\") + 1 : ])
    for el in os.listdir():
        try:
            os.chdir(startDir + "\\" + el)
            TreeFiles(startDir + "\\" + el, tab + 1)
        except NotADirectoryError:
            print("    " * (tab + 1), el)

homeDir = os.getcwd()
TreeFiles(homeDir, 0)
