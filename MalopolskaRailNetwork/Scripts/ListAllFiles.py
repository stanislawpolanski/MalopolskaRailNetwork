import os
from os import path
mainDirectoryPath = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork'

for files in os.listdir(mainDirectoryPath):
    print(files, os.path.isdir(os.path.join(mainDirectoryPath, files)))
