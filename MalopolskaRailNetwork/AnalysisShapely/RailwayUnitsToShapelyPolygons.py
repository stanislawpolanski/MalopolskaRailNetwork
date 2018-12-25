from shapely.geometry import Polygon
import Deserialisers.RailwayUnitsDeserialiser as rud
import numpy as np

railwayUnits = rud.railwayUnitsList

for ru in railwayUnits:
    geometriesList = []
    for geomString in ru['GEOM'].split(' '):
        (x, y) = (float(geomString.split(',')[0]), float(geomString.split(',')[1]))
        geometriesList.append([x, y])

    shapelyPolygon = Polygon(np.array(geometriesList))
