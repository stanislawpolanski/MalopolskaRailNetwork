import src.Constants.ProjectPaths

stationsPath = src.Constants.ProjectPaths.ProjectPathsStore.JSONDataFolder.value
stationsPath += "\\" + 'Railways.json'

import Deserialisers.JSONDeserializer

railwaysList = Deserialisers.JSONDeserializer.deserialize(stationsPath)
