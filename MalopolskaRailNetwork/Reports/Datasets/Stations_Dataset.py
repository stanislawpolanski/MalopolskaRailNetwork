import Reports.ReportMergedStations as SourceOfStations
import DataReaders.wwwReaders.wwwReader as SourceOfRelationships
import Reports.Datasets.RailwayUnits_Dataset as SourceOfRailwaysUnits
import Reports.Datasets.Railways_Dataset as SourceOfRailways

stations = SourceOfStations.returnMergedStations()
relationships = SourceOfRelationships.returnObjectsToRailwaysList()
railwayUnits = SourceOfRailwaysUnits.ReturnUnitsDataset()
railways = SourceOfRailways.ReturnRailwaysDataset()

Hashtable_Railways = dict()

for r in railways:
    Hashtable_Railways[r['Number']] = r['Id']


Hasthable_railwayUnits = dict()

for u in railwayUnits:
    Hasthable_railwayUnits[u['Name']] = u['Id']

Stations_Dataset = []
Geometries_Dataset = []
Relationships_Dataset = []

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
index_geometries = 30000
index_relationships = 1

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
    #todo extract typeofapoint
    #read out rest of the wms data
    if((s['WMSData'] is not None) and ('LocationPoints' in s['WMSData']) and (s['WMSData']['LocationPoints'] is not None)):
        for point in s['WMSData']['LocationPoints']:
            rel = dict()
            rel['Id'] = index_relationships
            rel['BeginningKmpost'] = float(point['KM_POCZ'])
            rel['CentreKmpost'] = float(point['KM_OSI'])
            rel['EndingKmpost'] = float(point['KM_KONC'])
            rel['RaiwalyId'] = int(Hashtable_Railways[int(point['NUMER_LINII'])])
            rel['GeometriesId'] = index_geometries
            #GeometryId [optional] - FK to geometries
            geom = dict()
            geom['Id'] = index_geometries
            geom['Value'] = point['GEOM']

            index_relationships += 1
            index_geometries += 1
            Geometries_Dataset.append(geom)
            Relationships_Dataset.append(rel)

    #print out geometries into seperate table
    #read in db relations

print('done so far')
#TODO
#process each station and create full relations list