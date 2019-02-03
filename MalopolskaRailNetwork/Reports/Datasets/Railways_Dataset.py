#Read and write to final dataset railway. Split into railways & geometries dataset. Ids of geometries starts with 20000. Child of #5
#read stations
def GetRailways_List():
    import Reports.Auxiliary.GetStationsAndRailwaysSnapshots as RailwaysSource
    Railways = RailwaysSource.GetRailwaysSnapshot_List()

    import ManuallyCreated.NonExistingPLKRailwaysInTheRegionIntTheWWW as NonExistingSource
    NonExisting = NonExistingSource.returnNonExistingRailwaysNumbers()

    for x in NonExisting:
        for r in Railways:
            if(x == int(r['Number'])):
                r['Geometry'] = None

    return Railways