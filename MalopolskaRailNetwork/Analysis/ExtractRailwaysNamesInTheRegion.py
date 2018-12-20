import Analysis.IntersectStationsFromWMSAggregatedAndCSV as extract
stationsInTheRegion = extract.returnWMSAggregatedStationsPresentInCSV()

railwaysInTheRegionNamesDict = dict()

#name - name
#stationsInTheRegion[name] - other data

for name in stationsInTheRegion:
    for location in stationsInTheRegion[name]['LocationPoints']:
        railwaysInTheRegionNamesDict[location['NUMER_LINII']] = location['NAZWA_LINII']

def returnNamesAndNumbersOfTheRailwaysInTheRegionDict():
    return railwaysInTheRegionNamesDict