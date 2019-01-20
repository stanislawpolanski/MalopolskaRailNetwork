import DataReaders.wwwReaders.wwwReader as reader

stations = reader.stationsDBList
railways = reader.returnRailwayList()
relations = reader.objectsToRailwaysDBList

#create hashmap railway number => railway id
railwaysNumberToIdDict = dict()
for r in railways:
    railwaysNumberToIdDict[r['Number']] = r['Id']

#create hashmap station name => station id
stationsNameToIdDict = dict()
for s in stations:
    stationsNameToIdDict[s['Name']] = s['Id']

def ifRelationExists(stationName, railwayNumber):
    railwayId = findRailwayId(railwayNumber)
    if(railwayId == -1):
        return False

    stationId = findStationId(stationName)
    if(stationId == -1):
        return False

    for rel in relations:
        if(rel['ObjectId'] == stationId and rel['LineId'] == railwayId):
            return True

    return False

def findRailwayId(number):
    key = str(number)
    if key in railwaysNumberToIdDict:
        return railwaysNumberToIdDict[key]
    return -1

def findStationId(name):
    if name in stationsNameToIdDict:
        return stationsNameToIdDict[name]
    return -1