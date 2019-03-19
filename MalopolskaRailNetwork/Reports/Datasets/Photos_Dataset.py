import DataReaders.wwwReaders.wwwReader as SourceOfPhotos
PhotosRaw = SourceOfPhotos.returnPhotosList()

Photos_Dataset = []

for p in PhotosRaw:
    photo = dict()
    photo['Id'] = p['Id']
    photo['AdditionDateTime'] = p['AdditionDateTime']
    photo['FilePath'] = p['FilePath']
    photo['Description'] = p['Description']

    Photos_Dataset.append(photo)

def ReturnPhotosDataset():
    return Photos_Dataset

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\Photos_Dataset.json'

jst.JSONSerialize(Photos_Dataset, path)
print("serialising done - photos")
