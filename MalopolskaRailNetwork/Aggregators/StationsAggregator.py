import Deserialisers.StationsDeserialize
import src.OnChangePrinter
import Data.Objects.PointOnARailway


stationsList = Deserialisers.StationsDeserialize.returnStationsList()

notifier = src.OnChangePrinter.OnChangePrinter(len(stationsList))

for station in stationsList:
    name = station['NAZWA']
    stationsAgg = dict()

    p = Data.Objects.PointOnARailway.PointOnARailway()
    #fill data

    if name in stationsAgg:
        stationsAgg[name] += 1
    else:
        stationsAgg[name] = 1

    #notify changes
    notifier.StepMade()