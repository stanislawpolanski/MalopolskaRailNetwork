import os
from os import path
import src.Paths
mainDirectoryPath = src.Paths.GetMainDirectoryPath()

def ListFiles(paths):
    for files in os.listdir(paths):
        newPath = paths + "\\" + files
        if os.path.isdir(os.path.join(newPath)):
            ListFiles(newPath)
        else:
            print(newPath.replace("\\", "\\\\"))
            
ListFiles(mainDirectoryPath)