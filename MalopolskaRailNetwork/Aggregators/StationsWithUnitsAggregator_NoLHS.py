import Deserialisers.StationsDeserialize
import src.OnChangePrinter
import Data.Objects.PointOnARailway
import Data.Objects.Station
import AnalysisShapely.Products.LoadIntersectedStations

stationsWithUnitsList = AnalysisShapely.Products.LoadIntersectedStations.ReturnStationsIntersectedWithUnits()

notifier = src.OnChangePrinter.OnChangePrinter(len(stationsWithUnitsList))

stationsWithUnitsAggregatedByLocation_NoLHS = dict()

for station in stationsWithUnitsList:
    isLHS = False
    if(station['NUMER_LINII'] == '65'):
        continue

    name = station['NAZWA']

    p = dict()
    p['GEOM'] = station['GEOM']
    p['KM_KONC'] = station['KM_KONC']
    p['KM_OSI'] = station['KM_OSI']
    p['KM_POCZ'] = station['KM_POCZ']
    p['NAZWA_LINII'] = station['NAZWA_LINII']
    p['NUMER_LINII'] = station['NUMER_LINII']
    
    p['ShapelyPoint'] = station['ShapelyPoint']

    if name not in stationsWithUnitsAggregatedByLocation_NoLHS:
        s = dict()
        s['RODZAJ'] = station['RODZAJ']
        s['NAZWA_ZAKLADU'] = station['NAZWA_ZAKLADU']
        stationsWithUnitsAggregatedByLocation_NoLHS[name] = s
        s['LocationPoints'] = []

    stationsWithUnitsAggregatedByLocation_NoLHS[name]['LocationPoints'].append(p)
    

    #notify changes
    #notifier.StepMade()

def returnAggregatedStationsWithUnitsDict_NoLHS():
    return stationsWithUnitsAggregatedByLocation_NoLHS
