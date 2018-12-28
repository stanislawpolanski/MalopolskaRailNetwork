import shapely
import src.OnChangePrinter as ocp

import AnalysisShapely.RailwayUnitsToShapelyPolygons as unitsWithPolygonsSource
import AnalysisShapely.RawStationsToShapelyPoints as stationsPointsSource

units = unitsWithPolygonsSource.returnRailwayUnitsWithShapelyPolygons()
stations = stationsPointsSource.returnStationsWithShapelyPoints()

stations = stations[69:100]

totalStationsNumber = len(stations)
printer = ocp.OnChangePrinter(totalStationsNumber)


def Intersect():
    for s in stations:
        for u in units:
            x = s['ShapelyPoint'].intersection(u['ShapelyPolygon'])
            if(not x.is_empty):
                s['NAZWA_ZAKLADU'] = u['ZAKLAD']
        if 'NAZWA_ZAKLADU' not in s:
            s['NAZWA_ZAKLADU'] = None
            print(s['NAZWA'])
        printer.StepMade()

def returnIntersection():
    return stations
