import Analysis.IntersectWMSWithWWW.IntersectStationsFromWMSWithWWW_NoLHS as matchesSource
matches = matchesSource.getAllMatches() #db - wms
dbAll = matchesSource.getUpdatedDB()

import AuxiliaryFunctions.DecapitalizeString as decap

#decapitalize names
for s in dbAll:
    if(int(s['Id']) > 9999):
        s['Name'] = decap.DecapitalizeString(s['Name'])



#todo develop

def printJsonRows():
    for s in dbAll:
        print(s)