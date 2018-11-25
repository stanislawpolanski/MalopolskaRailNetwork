import os
from os import path


filesPathsList = []

def FilesLister(paths):
    for files in os.listdir(paths):
        newPath = paths + "\\" + files
        if os.path.isdir(os.path.join(newPath)):
            FilesLister(newPath)
        else:
            filesPathsList.append(newPath.replace("\\", "\\\\"))