import matplotlib.pyplot as plt
import AnalysisShapely.RailwayUnitsToShapelyPolygons as ru

def PrepareRailwayUnitsPlot():
    railwayUnits = ru.returnRailwayUnitsWithShapelyPolygons()

    for u in railwayUnits:
        geom = u['ShapelyPolygon']
    
        x, y = geom.exterior.xy

        x = x.tolist()
        y = y.tolist()

        plt.plot(x, y)

def PlotRailwayUnits():
    plt.show()

def ReturnRailwayUnitsPlot():
    return plt