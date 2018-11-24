import os
from os import path
import src.Constants.ProjectPaths
mainDirectoryPath = src.Constants.ProjectPaths.ProjectPathsStore.Main.value

def ListFiles(paths):
    for files in os.listdir(paths):
        newPath = paths + "\\" + files
        if os.path.isdir(os.path.join(newPath)):
            ListFiles(newPath)
        else:
            print(newPath.replace("\\", "\\\\"))
            
ListFiles(mainDirectoryPath)