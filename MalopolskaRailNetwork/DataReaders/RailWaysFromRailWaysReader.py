import src.Constants.ProjectPaths
from xml.dom.minidom import parse

sourceFileName = 'WMS_SILK_linie_kolejowe.xml'

sourceFilesPath = src.Constants.ProjectPaths.ProjectPathsStore.XMLSourceDataFolder.value
sourceFilesPath = sourceFilesPath + str('\\') + sourceFileName

entityNodeName = 'SILK:WMS_SILK_linie_kolejowe'

dom = parse(sourceFilesPath)

railWayNodes = dom.getElementsByTagName(entityNodeName)

railWayList = []

for node in railWayNodes:
    currentRailWay = dict()
    for cn in node.childNodes:
        if(cn.localName == 'GEOM'):
            currentRailWay[cn.localName] = cn.getElementsByTagName('gml:coordinates')[0].firstChild.nodeValue
        else:
            currentRailWay[cn.localName] = cn.firstChild.nodeValue
    railWayList.append(currentRailWay)