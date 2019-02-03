#FUNCTIONS

#read railway units from WMS
def GetUnitsSourceList():
    import DataReaders.RailwaysUnitFromRailwaysUnitReader as UnitsDatasource
    Units = UnitsDatasource.listOfRailwaysUnits

    return Units

#read stations
def GetStationsList():
    import Reports.Auxiliary.GetStationsAndRailwaysSnapshots as StationsSource
    Stations = StationsSource.GetStationsListSnapshot()

    return Stations

#find units present in stations
#create railway units dataset due to agreement
#create geometries dataset (id from 10000) aa

#WORK