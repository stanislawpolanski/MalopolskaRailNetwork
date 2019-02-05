import Reports.ReportMergedStations as SourceOfStations
import DataReaders.wwwReaders.wwwReader as SourceOfRelationships

stations = SourceOfStations.returnMergedStations()
relationships = SourceOfRelationships.returnObjectsToRailwaysList()

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
#TODO
#process each station and create full relations list