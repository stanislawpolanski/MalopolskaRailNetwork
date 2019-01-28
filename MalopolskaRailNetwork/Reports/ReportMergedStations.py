import Analysis.IntersectWMSWithWWW.IntersectStationsFromWMSWithWWW_NoLHS as matchesSource
matches = matchesSource.getDbToWmsMatchesDict() #key:db - value:wms
dbAll = matchesSource.getUpdatedDB()

import Aggregators.StationsWithUnitsAggregator as aggSource
agg = aggSource.returnAggregatedStationsWithUnitsDict()

import AuxiliaryFunctions.DecapitalizeString as decap

for s in dbAll:
    name = s['Name']
    if(name in matches and (matches[name] is not None)):
        wmsData = agg[matches[name]]
        s['WMSData'] = wmsData
    else:
        s['WMSData'] = None

    if(int(s['Id']) > 9999):
        s['Name'] = decap.DecapitalizeString(s['Name'])


#todo REVISE

def printJsonRows():
    for s in dbAll:
        print(s)

def printShortJsonRows():
    for s in dbAll:
        stemp = s
        if(stemp['WMSData'] is not None):
            s['WMSData'] = 'WMS data present'
        print(stemp)

def returnMergedStations():
    return dbAll
