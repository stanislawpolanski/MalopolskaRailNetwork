import src.Constants.ProjectPaths

main = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
jsonPath = main + "\\AnalysisShapely\\Products\\StationsIntersectedWithUnits.json"

import src.JSONTool
stationsIntersectedWithUnits = src.JSONTool.JSONDeserialize(jsonPath)
