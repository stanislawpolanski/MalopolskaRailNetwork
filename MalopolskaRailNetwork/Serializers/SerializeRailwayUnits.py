from DataReaders import StationsReader
import os.path


with open(output, 'w+') as outfile:
    json.dump(railwayUnitsList, outfile)

