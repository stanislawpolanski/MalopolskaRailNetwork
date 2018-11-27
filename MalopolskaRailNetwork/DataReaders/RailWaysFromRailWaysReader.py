import src.Constants.ProjectPaths
import DataReaders.PLKXMLDataToListReader

sourceFileName = 'WMS_SILK_linie_kolejowe.xml'

sourceFilesPath = src.Constants.ProjectPaths.ProjectPathsStore.XMLSourceDataFolder.value
sourceFilesPath = sourceFilesPath + str('\\') + sourceFileName

entityNodeName = 'SILK:WMS_SILK_linie_kolejowe'

listOfRailways = DataReaders.PLKXMLDataToListReader.ReadFullNodesToList(sourceFilesPath, entityNodeName)



