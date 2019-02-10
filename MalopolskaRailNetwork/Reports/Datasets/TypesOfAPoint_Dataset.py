import Reports.ReportMergedStations as SourceOfStations
stations = SourceOfStations.returnMergedStations()

Hashset = set()

for s in stations:
    if(s['WMSData'] is not None):
        NameOfAType = s['WMSData']['RODZAJ']
        Hashset.add(NameOfAType)

TypesOfAPoint_Dataset = []

index = 1

for t in Hashset:
    SingleType = dict()
    SingleType['Id'] = index
    SingleType['AbbreviatedName'] = t

    TypesOfAPoint_Dataset.append(SingleType)

    index += 1

def ReturnTypesOfAPointDataset():
    return TypesOfAPoint_Dataset

def ReturnHashtableNamesToIds():
    Hashtable = dict()
    for t in TypesOfAPoint_Dataset:
        Hashtable[t['AbbreviatedName']] = t['Id']

    return Hashtable
