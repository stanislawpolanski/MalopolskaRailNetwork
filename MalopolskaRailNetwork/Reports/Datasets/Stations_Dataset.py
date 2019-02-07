import Reports.ReportMergedStations as SourceOfStations
import DataReaders.wwwReaders.wwwReader as SourceOfRelationships
import Reports.Datasets.RailwayUnits_Dataset as SourceOfRailwaysUnits

stations = SourceOfStations.returnMergedStations()
relationships = SourceOfRelationships.returnObjectsToRailwaysList()
railwayUnits = SourceOfRailwaysUnits.ReturnUnitsDataset()
Hasthable_railwayUnits = dict()

for u in railwayUnits:
    Hasthable_railwayUnits[u['Name']] = u['Id']

Stations_Dataset = []

#correct Olkusz
i = 0
for x in stations:
    if(stations[i]['Name'] == 'Olkusz'):
        OlkuszPlk_index = i 
    if(stations[i]['Name'] == 'Olkusz LHS'):
        OlkuszLhs_index = i 
    i += 1

PlkLocation = stations[OlkuszPlk_index]['WMSData']['LocationPoints'][0]
LhsLocation = stations[OlkuszPlk_index]['WMSData']['LocationPoints'][1]

stations[OlkuszPlk_index]['WMSData']['LocationPoints'].remove(LhsLocation)

stations[OlkuszLhs_index]['WMSData'] = dict()
stations[OlkuszLhs_index]['WMSData']['RODZAJ'] = 'PO'
stations[OlkuszLhs_index]['WMSData']['NAZWA_ZAKLADU'] = None
stations[OlkuszLhs_index]['WMSData']['LocationPoints'] = []
stations[OlkuszLhs_index]['WMSData']['LocationPoints'].append(LhsLocation)
#enrich stations with DB relations, otherwise DB relations = None
for s in stations:
    Station = dict()
    Station['Id'] = int(s['Id'])
    Station['Name'] = s['Name']
    Station['OwnerId'] = int(s['OwnerId'])
    #read railway unit and type of a point
    if((s['WMSData'] is not None) and ('NAZWA_ZAKLADU' in s['WMSData']) and (s['WMSData']['NAZWA_ZAKLADU'] is not None)):
        Station['RailwayUnitId'] = Hasthable_railwayUnits[s['WMSData']['NAZWA_ZAKLADU']]
    else:
        Station['RailwayUnitId'] = None
    #read out rest of the wms data
    #read in db relations

print('done so far')
#TODO
#process each station and create full relations list