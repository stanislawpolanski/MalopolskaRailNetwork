import Deserialisers.StationsDeserialize
import src.OnChangePrinter
import Data.Objects.PointOnARailway
import Data.Objects.Station


stationsList = Deserialisers.StationsDeserialize.returnStationsList()

notifier = src.OnChangePrinter.OnChangePrinter(len(stationsList))

stationsAgg = dict()

for station in stationsList:
    name = station['NAZWA']

    p = dict()
    p['GEOM'] = station['GEOM']
    p['KM_KONC'] = station['KM_KONC']
    p['KM_OSI'] = station['KM_OSI']
    p['KM_POCZ'] = station['KM_POCZ']
    p['NAZWA_LINII'] = station['NAZWA_LINII']
    p['NUMER_LINII'] = station['NUMER_LINII']

    if name not in stationsAgg:
        s = dict()
        s['RODZAJ'] = station['RODZAJ']
        stationsAgg[name] = s
        s['LocationPoints'] = []

    stationsAgg[name]['LocationPoints'].append(p)

    #notify changes
    notifier.StepMade()