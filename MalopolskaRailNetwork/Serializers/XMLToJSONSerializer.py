import os.path
import json

def SerializeDictsListToXML(list, pathToTheOutputFile):
    #check whetever output file exists, if so then exits the function in case not to overwrite/erase existing data
    if(os.path.isfile(pathToTheOutputFile)):
        return
    
    with open(pathToTheOutputFile, 'w+') as outfile:
        json.dump(list, outfile)