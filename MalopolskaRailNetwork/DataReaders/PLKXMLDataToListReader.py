import src.Constants.ProjectPaths
from xml.dom.minidom import parse

def ReadFullNodesToList(filePath, nodeName):
    dom = parse(filePath)
    XMLNodes = dom.getElementsByTagName(nodeName)
    nodesList = []

    for node in XMLNodes:
        currentNodeToList = dict()
        for cn in node.childNodes:
            if(cn.localName == 'GEOM'):
                currentNodeToList[cn.localName] = cn.getElementsByTagName('gml:coordinates')[0].firstChild.nodeValue
            else:
                currentNodeToList[cn.localName] = cn.firstChild.nodeValue
        nodesList.append(currentNodeToList)
    return nodesList

