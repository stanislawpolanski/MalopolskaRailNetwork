import json

def deserialize(path):
    with open(path) as jsonFile:
        return json.load(jsonFile)