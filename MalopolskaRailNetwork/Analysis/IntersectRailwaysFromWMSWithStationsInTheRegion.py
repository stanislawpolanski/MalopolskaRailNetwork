import Analysis.ExtractRailwaysNamesInTheRegion as rNamesInReg
railwaysNamesInTheRegion = rNamesInReg.returnNamesAndNumbersOfTheRailwaysInTheRegionDict()

import DataReaders.RailWaysFromRailWaysReader as rAll
railways = rAll.DataReaders.RailWaysFromRailWaysReader.returnListOfRailways()

railwaysInTheRegion = []

for rNumber in railwaysNamesInTheRegion:
    for rFull in railways:
        if(rNumber == rFull['NUMER']):
            #print('match')
            railwaysInTheRegion.append(rFull)

def returnRailwaysInTheRegion():
    return railwaysInTheRegion