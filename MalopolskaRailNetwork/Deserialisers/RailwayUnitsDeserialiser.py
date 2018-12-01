import src.Constants.ProjectPaths

stationsPath = src.Constants.ProjectPaths.ProjectPathsStore.JSONDataFolder.value
stationsPath += "\\" + 'RailwayUnits.json'

import Deserialisers.JSONDeserializer

railwayUnitsList = Deserialisers.JSONDeserializer.deserialize(stationsPath)
