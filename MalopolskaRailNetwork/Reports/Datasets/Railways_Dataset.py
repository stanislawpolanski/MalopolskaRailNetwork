#Read and write to final dataset railway. Split into railways & geometries dataset. Ids of geometries starts with 20000. Child of #5
#read stations
import Reports.Auxiliary.GetStationsAndRailwaysSnapshots as RailwaysSource
RailwaysRaw = RailwaysSource.GetRailwaysSnapshot_List()

import ManuallyCreated.NonExistingPLKRailwaysInTheRegionIntTheWWW as NonExistingSource
NonExisting = NonExistingSource.returnNonExistingRailwaysNumbers()

    #iterate on railway raw, rewrite 118

Railways_Dataset = []
Geometries_Partial_Dataset = []

def ProcessDatasets():

    #index for geometries
    index = 20000

    for r in RailwaysRaw:
        #if 118, then id+10000, name to Kraków Lotnisko, save ID
        #Nowy Targ - Podczerwone with ID aa
        if(int(r['Number']) == 118):
            r['Id'] = 10118
            r['Name'] = 'Kraków Główny - Kraków Lotnisko'

            old = dict()
            old['Id'] = 28
            old['Name'] = 'Nowy Targ - Podczerwone'
            old['OwnerId'] = 1
            old['Number'] = 118
            old['Geometry'] = None

            RailwaysRaw.append(old)
            break

    for r in RailwaysRaw:
        #basic rewrite
        new = dict()
        new['Id'] = int(r['Id'])
        new['Name'] = r['Name']
        new['Number'] = int(r['Number'])
        new['OwnerId'] = int(r['OwnerId'])

        if(r['Geometry'] is None):
            new['GeometryId'] = None
        else:
            new['GeometryId'] = index

            geometry = dict()
            geometry['Id'] = index
            geometry['Value'] = r['Geometry']

            index += 1

        Railways_Dataset.append(new)
        Geometries_Partial_Dataset.append(geometry)


def ReturnRailwaysDataset():
    ProcessDatasets()
    return Railways_Dataset

def ReturnGeometriesPartialDataset():
    ProcessDatasets()
    return Geometries_Partial_Dataset