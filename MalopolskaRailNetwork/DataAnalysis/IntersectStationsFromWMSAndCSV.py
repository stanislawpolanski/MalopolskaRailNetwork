#DataReaders/StationsReader.py
import DataReaders.StationsReader
wmsStationsList = DataReaders.StationsReader.returnWMSStationsList()
#DataReaders/CSVReader/CSVReader.py
import DataReaders.CSVReader.CSVReader
csvStationsList = DataReaders.CSVReader.CSVReader.returnCSVStationsList()

#now intersect both datasets, keep fields of wms stations
count = 0

wmsStationsPresentInBothWMSAndCSVList = []

for csv in csvStationsList:
    for wms in wmsStationsList:
        count += 1
        if(csv == wms['NAZWA']):
            wmsStationsPresentInBothWMSAndCSVList.append(wms)
            break

print('total steps of', count)