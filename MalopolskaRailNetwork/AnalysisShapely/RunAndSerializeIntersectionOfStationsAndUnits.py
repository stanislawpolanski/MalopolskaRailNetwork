import src.Constants.ProjectPaths

import AnalysisShapely.IntersectionOfStationsWithUnits as intersect

intersect.Intersect()
stations = intersect.returnIntersection()

main = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
jsonPath = main + "\\AnalysisShapely\\Products\\StationsIntersectedWithUnits.json"

import src.JSONTool

src.JSONTool.JSONSerialize(stations, jsonPath)