import src.Constants.ProjectPaths

stationsPath = src.Constants.ProjectPaths.ProjectPathsStore.JSONDataFolder.value
stationsPath += "\\" + 'Stations.json'

import Deserialisers.JSONDeserializer

stationsList = Deserialisers.JSONDeserializer.deserialize(stationsPath)