#import decapitalazing function
import AuxiliaryFunctions.DecapitalizeString as decap

#import data
import Analysis.IntersectWMSWithWWW.IntersectRailwaysFromWMSWithWWW_NoLHS as source
data = source.returnFinalBasicRailwaysRowSet()

#import wms as a hashmap with key = railway number
import DataReaders.RailWaysFromRailWaysReader as wmsSource
wmsData = wmsSource.returnListOfRailways()

wmsDict = dict()

for r in wmsData:
    wmsDict[int(r['NUMER'])] = r

#enrich data with additional info from WMS (like geometries), decapitalize letters
for railway in data:
    railway['Name'] = decap.DecapitalizeString(railway['Name'])

    if(int(railway['OwnerId']) in [1, 16] and int(railway['Number']) in wmsDict):
        railway['Geometry'] = wmsDict[int(railway['Number'])]['GEOM']
        continue

    railway['Geometry'] = None

#sort by railway number
data.sort(key = lambda x: int(x['Number']))

#return function
def returnMergedRailways():
    return data

#report printing with no geometries
def printShortReport():
    for r in data:
        print(r['Number'], r['Name'])

