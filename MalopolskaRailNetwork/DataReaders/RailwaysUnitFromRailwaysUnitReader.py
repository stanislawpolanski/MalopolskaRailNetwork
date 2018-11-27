import src.Constants.ProjectPaths
import DataReaders.PLKXMLDataToListReader

#define input names
sourceFileName = 'WMS_SILK_zaklady.xml'
entityNodeName = 'SILK:WMS_SILK_zaklady'

sourceFilesPath = src.Constants.ProjectPaths.ProjectPathsStore.XMLSourceDataFolder.value
sourceFilesPath = sourceFilesPath + str('\\') + sourceFileName

listOfRailwaysUnits = DataReaders.PLKXMLDataToListReader.ReadFullNodesToList(sourceFilesPath, entityNodeName)