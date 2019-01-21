#read relations from www
import DataReaders.wwwReaders.wwwReader as wwwReader
relationsDB = wwwReader.returnObjectsToRailwaysList()
#read stations (they have railways info) - which file
import Analysis.IntersectStationsWithUnitsAggregatedAndCSV as stationsSource
stationsWithRailwaysWMS = stationsSource.returnStationsWithUnitsAggregatedInTheRegionDict()
#helper variable for new id's
i = 10000
#initialize final relations list
stationsNamesToRailwaysNumbers = []
#import onchange printer
import src.OnChangePrinter as ocpSource
notifier = ocpSource.OnChangePrinter(311)
#import stations db to stations wms
import Analysis.IntersectWMSWithWWW.IntersectStationsFromWMSWithWWW_NoLHS as matchesSource
matches = matchesSource.getAllMatches()
#reverse stations db to stations wms
#then it comes to: stations wms -> stations db
wmsToDB = dict()
for x in matches:
    wmsToDB[x[1]] = x[0]

#import relation checker
import AuxiliaryFunctions.CheckIfRelationBetweenStationsAndRailwayExistsInDB as checker

#loop through all relations in station file
#todo THOSE BIG LETTERS =>>> SHOULD BE SMALL - FIND A BUG
#todo something with matches???
for key in stationsWithRailwaysWMS:
    for relation in stationsWithRailwaysWMS[key]['LocationPoints']:
        railwayNumber = relation['NUMER_LINII']
        if(railwayNumber == '65'):
            #notifier.StepMade()
            continue
        stationName = wmsToDB[key]

        relationExists = checker.ifRelationExists(stationName, railwayNumber)
        #if relationExists is false then append relation
        if(not relationExists):
            stationsNamesToRailwaysNumbers.append([stationName, railwayNumber])
        #notifier.StepMade()

print('done')
#todo return result
def returnLackingInDBstationsNamesToRailwaysNumbers():
    return stationsNamesToRailwaysNumbers