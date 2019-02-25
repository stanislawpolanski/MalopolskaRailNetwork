import DataReaders.wwwReaders.wwwReader as SourceOwners
OwnersRaw = SourceOwners.ownersDBList

Owners_Dataset = []

for o in OwnersRaw:
    owner = dict()
    owner['Id'] = o['Id']
    owner['Name'] = o['Name']

    Owners_Dataset.append(owner)

def ReturnOwnersDataset():
    return Owners_Dataset

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\Owners_Dataset.json'

jst.JSONSerialize(Owners_Dataset, path)
print("serialising done")