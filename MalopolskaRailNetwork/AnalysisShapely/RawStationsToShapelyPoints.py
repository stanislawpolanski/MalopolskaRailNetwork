from shapely.geometry import Point

import Deserialisers.StationsDeserialize as srd
stations = srd.returnStationsList()

for s in stations:
    x = float(s['GEOM'].split(',')[0])
    y = float(s['GEOM'].split(',')[1])    
    
    p = Point(x, y)

    s['ShapelyPoint'] = p

def returnStationsWithShapelyPoints():
    return stations


