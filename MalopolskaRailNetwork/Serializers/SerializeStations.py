from DataReaders import StationsReader

DataReaders.StationsReader

with open(output, 'w+') as outfile:
    json.dump(stationsList, outfile)
