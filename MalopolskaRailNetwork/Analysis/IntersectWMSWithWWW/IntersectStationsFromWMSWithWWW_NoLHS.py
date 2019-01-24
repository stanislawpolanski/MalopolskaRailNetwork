#string comparer
import AuxiliaryFunctions.StringsSimilarityCalculator as similarityCalculator

#read wms
import Analysis.IntersectStationsWithUnitsAggregatedAndCSV_NoLHS as stationsSource
wmsDict = stationsSource.returnStationsWithUnitsAggregatedInTheRegionDict_NoLHS()

#import non existing stations
import ManuallyCreated.NonExistingPLKStationsInTheRegionInTheWWW as nes
nonExistingStationsList = nes.returnList()

#read db
import DataReaders.wwwReaders.wwwReader as wmsSource
dbSource = wmsSource.stationsDBList
dbAll = dbSource
dbPLK = []
dbLHS = []

#extract PLK and LHSstations
for x in dbAll:
    if(x['OwnerId'] == '1'):
        dbPLK.append(x)
    if(x['OwnerId'] == '16'):
        dbLHS.append(x)

#initialize final rowset
result = dbPLK

#helper variable for new id's in final rowset
i = 10000

#loop through db and find matches, kick out matched in wms
listOfMatches = []
wmsMatched = set()

for d in dbPLK:
    previousRatio = 0
    currentMatch = None

    dbName = d['Name']

    for key in wmsDict:
        if(dbName in nonExistingStationsList):
            break

        currentRatio = similarityCalculator.GetStringsSimilarityRatio(dbName, key)
        if(currentRatio > previousRatio):
            currentMatch = key
            previousRatio = currentRatio

    match = [d['Name'], currentMatch, previousRatio] #db name, wms name, ratio
    wmsMatched.add(currentMatch)
    listOfMatches.append(match)


for key in wmsDict:
    if(key in wmsMatched):
        continue
    s = dict()
    s['name'] = 'objects'
    s['Id'] = i
    s['TypeId'] = 1 #typeid = 1 - means station, typeid = 2 means rolling stock
    s['OwnerId'] = 1 #this one is PLK
    s['Name'] = key
    #add to dbAll
    dbAll.append(s)
    #update matches!
    listOfMatches.append([key, key, 2])
    #raise up i value
    i += 1

def printAllMatches():
    for x in listOfMatches:
        print(x)

def printNotExactMatches():
    for x in listOfMatches:
        if(x[2] < 1):
            print(x)

def printNoneMatches():
    for x in listOfMatches:
        if(x[1] == None):
            print(x)

def getMachesFound():
    matchesFound = []
    for x in listOfMatches:
        if(x[2] < 2):
            matchesFound.append(x)
    return matchesFound

def getAllMatches():
    return listOfMatches

def getUpdatedDB():
    return dbAll