


import DataReaders.wwwReaders.wwwReader as SourceOfPhotosToObjects
PhotosToObjectsRaw = SourceOfPhotosToObjects.returnPhotosToObjectsList()

PhotosToObjects_Dataset = []

for pto in PhotosToObjectsRaw:
    photoToObject = dict()
    photoToObject['Id'] = pto['Id']
    photoToObject['PhotoId'] = pto['PhotoId']
    photoToObject['ObjectId'] = pto['ObjectId']

    PhotosToObjects_Dataset.append(photoToObject)

def ReturnPhotosToObjectsDataset():
    return PhotosToObjects_Dataset

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\PhotosToObjects_Dataset.json'

jst.JSONSerialize(PhotosToObjects_Dataset, path)
print("serialising done - photos to objects")


