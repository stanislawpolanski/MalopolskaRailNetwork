import Aggregators.StationsWithUnitsAggregator as sua

data = sua.returnAggregatedStationsWithUnitsDict()

import src.Constants.ProjectPaths

main = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
path = main + "\\Products\\StationsWithUnitsAggregatedByLocation.json"

import src.JSONTool

src.JSONTool.JSONSerialize(data, path)