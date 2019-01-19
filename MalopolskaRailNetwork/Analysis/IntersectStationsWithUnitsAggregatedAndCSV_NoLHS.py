import Aggregators.StationsWithUnitsAggregator_NoLHS as aggF
import DataReaders.CSVReader.CSVReader as csvF

agg = aggF.returnAggregatedStationsWithUnitsDict_NoLHS()
csv = csvF.returnCSVStationsList()

stationsWithUnitsAggregatedInTheRegionDict = dict()

for sKey in agg:
    for c in csv:
        if(sKey == c):
            stationsWithUnitsAggregatedInTheRegionDict[sKey] = agg[sKey]

def returnStationsWithUnitsAggregatedInTheRegionDict_NoLHS():
    return stationsWithUnitsAggregatedInTheRegionDict