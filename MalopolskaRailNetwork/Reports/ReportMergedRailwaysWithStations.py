import src.Constants.ProjectPaths
pp = src.Constants.ProjectPaths.ProjectPathsStore.DataSnapshots.value

railwaysPath = pp + "\\railwaysSnapshot20190128.json"
stationsPath = pp + "\\stationsSnapshot20190128.json"

import src.JSONTool as jst

railways = jst.JSONDeserialize(railwaysPath)
stations = jst.JSONDeserialize(stationsPath)


for r in railways:
    num = r['Number']