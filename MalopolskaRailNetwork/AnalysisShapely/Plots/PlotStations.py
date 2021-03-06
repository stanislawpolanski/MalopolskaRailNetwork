import matplotlib.pyplot as plt
import AnalysisShapely.RawStationsToShapelyPoints as rs
import shapely.geometry

def PrepareStationsPlot():
    stations = rs.returnStationsWithShapelyPoints()

    x = []
    y = []

    for s in stations:
        p = s['ShapelyPoint']

        x.append(p.x)
        y.append(p.y)
    
    plt.plot(x, y, 'ro', markersize = 1)

def ReturnStationsPlot():
    return plt

def ShowStationsPlot():
    plt.show()