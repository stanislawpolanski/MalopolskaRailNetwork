#inputs:name
path = r'C:\Users\Dell\source\repos\MalopolskaRailNetwork\MalopolskaRailNetwork\SourceFiles\MSK\stacjecbapl20180912_1020.xml'

#parse xml and select 'table' nodes (those with data)
from xml.dom.minidom import parse
dom = parse(path)
xmlnodes = dom.getElementsByTagName('table')


#prepare lists
stationsDBList = []
ownersDBList = []
objectsToRailwaysDBList = []
railwaysDBList = []
rollingStockDBList = []
photosList = []
photosToObjectsList = []

#loop through xml to extract particular nodes
for n in xmlnodes:
	currentNodeToList = dict()

	currentNodeToList['name'] = n.getAttribute('name')

	elements = n.getElementsByTagName('column')

	for e in elements:
		key = e.getAttribute('name')
		currentNodeToList[key] = e.firstChild.nodeValue

	#extract railways
	if(currentNodeToList['name'] == 'railways'):
		railwaysDBList.append(currentNodeToList)
	#extract owners
	if(currentNodeToList['name'] == 'owners'):
		ownersDBList.append(currentNodeToList)
	#extract stations to objects
	if(currentNodeToList['name'] == 'objects_to_railways'):
		objectsToRailwaysDBList.append(currentNodeToList)
	#extract stations from objects
	if(currentNodeToList['name'] == 'objects' and currentNodeToList['TypeId'] == '1'):
		stationsDBList.append(currentNodeToList)

    #extract rolling stock from objects
	if(currentNodeToList['name'] == 'objects' and currentNodeToList['TypeId'] == '2'):
		rollingStockDBList.append(currentNodeToList)

	#extract photos
	if(currentNodeToList['name'] == 'photos'):
		photosList.append(currentNodeToList)

	#extract photos
	if(currentNodeToList['name'] == 'photos_to_objects'):
		photosToObjectsList.append(currentNodeToList)


def returnRailwayList():
    return railwaysDBList

def returnObjectsToRailwaysList():
    return objectsToRailwaysDBList

def returnRollingStockList():
    return rollingStockDBList

def returnPhotosList():
	return photosList

def returnPhotosToObjectsList():
	return photosToObjectsList