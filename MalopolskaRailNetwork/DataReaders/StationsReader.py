import src.Constants.ProjectPaths
from xml.dom.minidom import parse

sourceFileName = 'WMS_SILK_stacje_przystanki.xml'

sourceFilesPath = src.Constants.ProjectPaths.ProjectPathsStore.XMLSourceDataFolder.value
sourceFilesPath = sourceFilesPath + str('\\') + sourceFileName

entityNodeName = 'SILK:WMS_SILK_stacje_przystanki'

dom = parse(sourceFilesPath)

stationsNodes = dom.getElementsByTagName(entityNodeName)

stationsList = []
for node in stationsNodes:
    currentStation = dict()
    for cn in node.childNodes:
        if(cn.localName == 'GEOM'):
            currentStation[cn.localName] = cn.getElementsByTagName('gml:coordinates')[0].firstChild.nodeValue
        else:
            currentStation[cn.localName] = cn.firstChild.nodeValue
    stationsList.append(currentStation)

def returnWMSStationsList():
    return stationsList