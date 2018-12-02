import Deserialisers.StationsDeserialize

stationsList = Deserialisers.StationsDeserialize.returnStationsList()
lenght = len(stationsList)

i = 0
for station in stationsList:
    name = station['NAZWA']
    stationsAgg = dict()

    if name in stationsAgg:
        stationsAgg[name] += 1
    else:
        stationsAgg[name] = 1

    #notify changes
    i += 1
    print('working on station ', i , ' of ', lenght, ' which is ', round(i * 100 / lenght), '%' )
