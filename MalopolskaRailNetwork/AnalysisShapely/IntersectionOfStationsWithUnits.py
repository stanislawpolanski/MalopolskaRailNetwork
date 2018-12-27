import shapely
import src.OnChangePrinter as ocp

import AnalysisShapely.RailwayUnitsToShapelyPolygons as unitsWithPolygonsSource
import AnalysisShapely.RawStationsToShapelyPoints as stationsPointsSource

units = unitsWithPolygonsSource.returnRailwayUnitsWithShapelyPolygons()
stations = stationsPointsSource.returnStationsWithShapelyPoints()

totalStationsNumber = len(stations)
printer = ocp.OnChangePrinter(totalStationsNumber)

def Intersect():
    for s in stations:
        for u in units:
            x = s['ShapelyPoint'].intersection(u['ShapelyPolygon'])
            if(not x.is_empty):
                s['NAZWA_ZAKLADU'] = u['ZAKLAD']
                break
        if 'NAZWA_ZAKLADU' not in s:
            s['NAZWA_ZAKLADU'] = None
        printer.StepMade()

def returnIntersection():
    return stations
