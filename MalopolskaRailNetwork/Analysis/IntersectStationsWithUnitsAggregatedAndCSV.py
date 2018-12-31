import Aggregators.StationsWithUnitsAggregator as aggF
import DataReaders.CSVReader.CSVReader as csvF

agg = aggF.returnAggregatedStationsWithUnitsDict()
csv = csvF.returnCSVStationsList()

stationsWithUnitsAggregatedInTheRegionDict = dict()

for sKey in agg:
    for c in csv:
        if(sKey == c):
            stationsWithUnitsAggregatedInTheRegionDict[sKey] = agg[sKey]

def returnStationsWithUnitsAggregatedInTheRegionDict():
    return stationsWithUnitsAggregatedInTheRegionDict