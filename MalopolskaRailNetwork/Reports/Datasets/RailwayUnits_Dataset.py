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
#create geometries dataset (id from 10000) aa

#WORK