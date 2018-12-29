import src.Constants.ProjectPaths

main = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
path = main + "\\Products\\StationsWithUnitsAggregatedByLocation.json"

import src.JSONTool

data = src.JSONTool.JSONDeserialize(path)

def returnStationsWithUnitsAggregatedByLocation():
    return data