import os
from os import path
import src.Constants.ProjectPaths
mainDirectoryPath = src.Constants.ProjectPaths.ProjectPathsStore.Main.value

filesPathsList = []

def FilesLister(paths):
    for files in os.listdir(paths):
        newPath = paths + "\\" + files
        if os.path.isdir(os.path.join(newPath)):
            FilesLister(newPath)
        else:
            filesPathsList.append(newPath.replace("\\", "\\\\"))
            
FilesLister(mainDirectoryPath)