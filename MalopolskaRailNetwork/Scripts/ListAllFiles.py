import os
from os import path
mainDirectoryPath = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork'

def ListFiles(paths):
    for files in os.listdir(paths):
        newPath = paths + "\\" + files
        if os.path.isdir(os.path.join(newPath)):
            ListFiles(newPath)
        else:
            print(newPath)
            
ListFiles(mainDirectoryPath)