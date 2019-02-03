import src.Constants.ProjectPaths
pp = src.Constants.ProjectPaths.ProjectPathsStore.DataSnapshots.value
railwaysPath = pp + "\\railwaysSnapshot20190128.json"
stationsPath = pp + "\\stationsSnapshot20190128.json"
import src.JSONTool as jst

def GetStationsSnapshot_List():
    stations = jst.JSONDeserialize(stationsPath)
    return stations

def GetRailwaysSnapshot_List():
    railways = jst.JSONDeserialize(railwaysPath)
    return railways