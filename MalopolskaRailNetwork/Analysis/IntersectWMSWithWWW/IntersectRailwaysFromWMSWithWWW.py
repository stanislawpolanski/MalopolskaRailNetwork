#import wms railways
import Analysis.ExtractRailwaysNamesInTheRegion as wmsSource
wms = wmsSource.returnNamesAndNumbersOfTheRailwaysInTheRegionDict()

#import www railways
import DataReaders.wwwReaders.wwwReader as dbSource
db = dbSource.returnRailwayList()

#final database row set
finalRowSet = db

#variable for new entries in the database row set
i = 10000

#intersect

for wKey in wms:
    keyExistsInDB = False
    for dbr in db:
        match = (dbr['Number'] == wKey)
        if(match):
            #print('Following railway exists in the DB', wms[wKey])
            keyExistsInDB = True
            break
    if(not keyExistsInDB):
        #print('no corresponding railway:', wms[wKey])
        railway = dict()
        railway['name'] = 'railways'
        railway['Id'] = i + int(wKey)
        railway['OwnerId'] = 1
        railway['Number'] = wKey
        railway['Name'] = wms[wKey]

        finalRowSet.append(railway)


#return result
def returnFinalRailwaysRowSet():
    return finalRowSet
