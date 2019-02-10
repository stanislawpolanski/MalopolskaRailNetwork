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