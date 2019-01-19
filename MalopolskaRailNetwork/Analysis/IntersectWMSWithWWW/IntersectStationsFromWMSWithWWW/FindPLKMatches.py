#string comparer
import AuxiliaryFunctions.StringsSimilarityCalculator as similarityCalculator

#read wms
import Analysis.IntersectStationsWithUnitsAggregatedAndCSV as stationsSource
wmsDict = stationsSource.returnStationsWithUnitsAggregatedInTheRegionDict()

#import non existing stations
import Products.ManuallyCreated.NonExistingPLKStationsInTheRegionInTheWWW as nes
nonExistingStationsList = nes.returnList()

#read db
import DataReaders.wwwReaders.wwwReader as wmsSource
dbAll = wmsSource.stationsDBList
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

    match = [d['Name'], currentMatch, previousRatio]
    listOfMatches.append(match)
#todo filter data so PLK lines does not contain LHS geometry info

#todo extract those stations with line number = 65 - this one is LHS
#loop through remaining stations in wms and assign new ids

#extract 


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