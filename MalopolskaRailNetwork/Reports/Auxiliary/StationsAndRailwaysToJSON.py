railwaysPath = pp + "\\railwaysSnapshot20190128.json"
stationsPath = pp + "\\stationsSnapshot20190128.json"

#^^^PATHS UP HERE^^^

import Reports.ReportMergedRailways as railwaysSource
import Reports.ReportMergedStations as stationsSource

railways = railwaysSource.returnMergedRailways()
stations = stationsSource.returnMergedStations()

import src.Constants.ProjectPaths
pp = src.Constants.ProjectPaths.ProjectPathsStore.DataSnapshots.value

import src.JSONTool as jst

jst.JSONSerialize(stations, stationsPath)
jst.JSONSerialize(railways, railwaysPath)

