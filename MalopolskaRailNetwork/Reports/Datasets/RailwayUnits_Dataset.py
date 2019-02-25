#FUNCTIONS

#read railway units from WMS
def GetUnitsSource_List():
    import DataReaders.RailwaysUnitFromRailwaysUnitReader as UnitsDatasource
    Units = UnitsDatasource.listOfRailwaysUnits

    return Units

#read stations
def GetStations_List():
    import Reports.Auxiliary.GetStationsAndRailwaysSnapshots as StationsSource
    Stations = StationsSource.GetStationsSnapshot_List()

    return Stations

#find units present in stations

def ExtractUnitsInTheRegion_List():
    UnitsInTheRegion_Raw = []

    for Unit in GetUnitsSource_List():
        UnitName = Unit['ZAKLAD']
        Stations_List = GetStations_List()

        for station in Stations_List:
            if(station['WMSData'] is None):
                StationUnitName = 'Not available'
            else:
                StationUnitName = station['WMSData']['NAZWA_ZAKLADU']
            if(UnitName == StationUnitName):
                UnitsInTheRegion_Raw.append(Unit)
                break
    return UnitsInTheRegion_Raw
            
#create railway units dataset due to agreement
Geometries_Partial_Dataset = []
Units_Dataset = []

Units_Raw = ExtractUnitsInTheRegion_List()

index = 10000

for u in Units_Raw: 

    unit = dict()
    unit['Id'] = index
    unit['Name'] = u['ZAKLAD']
    unit['GeometriesId'] = index

    Units_Dataset.append(unit)

    geometry = dict()
    geometry['Id'] = index
    geometry['Value'] = u['GEOM']

    Geometries_Partial_Dataset.append(geometry)

    index += 1


def ReturnUnitsDataset():
    return Units_Dataset

def ReturnGeometriesPartialDataset():
    return Geometries_Partial_Dataset

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\RailwayUnits_Dataset.json'

jst.JSONSerialize(Units_Dataset, path)
print("serialising done")