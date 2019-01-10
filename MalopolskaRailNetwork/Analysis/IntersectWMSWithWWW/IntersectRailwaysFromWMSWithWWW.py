#import wms railways
import Analysis.ExtractRailwaysNamesInTheRegion as wmsSource

wms = wmsSource.returnNamesAndNumbersOfTheRailwaysInTheRegionDict()

#import www railways
import DataReaders.wwwReaders.wwwReader as dbSource

db = dbSource.returnRailwayList()

#intersect

for wKey in wms:
    keyExistsInDB = False
    for dbr in db:
        match = (dbr['Number'] == wKey)
        if(match):
            print('match of railway:', wms[wKey])
            keyExistsInDB = True
            break
    if(not keyExistsInDB):
        print('no corresponding railway:', wms[wKey])
    #TODO iteration ok - how to process data


#return result
