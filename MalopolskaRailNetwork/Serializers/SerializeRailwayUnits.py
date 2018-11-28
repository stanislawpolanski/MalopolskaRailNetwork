import src.Constants.ProjectPaths

main = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
jsonPath = main + "\\Data\\SourceDataInJSON\\Railways.json"

import DataReaders.RailWaysFromRailWaysReader

DataReaders.RailWaysFromRailWaysReader

import Serializers.XMLToJSONSerializer

Serializers.XMLToJSONSerializer.SerializeDictsListToXML(listOfRailways, jsonPath)