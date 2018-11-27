import src.Constants.ProjectPaths
from xml.dom.minidom import parse

class PLKXMLDataToListReader(object):
    """Reads to lists XML PLK files"""
    sourceFilePath = str()
    nodeName       = str()
    nodesList      = []

    def LoadFile(filePath):
        sourceFileName = filePath

    def ReadFullNodesToList(nodeName):
        XMLNodes = dom.getElementsByTagName(nodeName)

        for node in XMLNodes:
            currentNodeToList = dict()
            for cn in node.childNodes:
                if(cn.localName == 'GEOM'):
                    currentNodeToList[cn.localName] = cn.getElementsByTagName('gml:coordinates')[0].firstChild.nodeValue
                else:
                    currentNodeToList[cn.localName] = cn.firstChild.nodeValue
            nodesList.append(currentNodeToList)

