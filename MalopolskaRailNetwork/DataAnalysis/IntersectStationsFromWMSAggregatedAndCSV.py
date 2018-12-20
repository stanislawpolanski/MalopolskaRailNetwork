#DataReaders/StationsReader.py
import Aggregators.WMSStationsAggregator
wmsAggregatedStationsList = Aggregators.WMSStationsAggregator.returnAggregatedStationsDict()
#DataReaders/CSVReader/CSVReader.py
import DataReaders.CSVReader.CSVReader
csvStationsList = DataReaders.CSVReader.CSVReader.returnCSVStationsList()

#now intersect both datasets, keep fields of wms stations
count = 0

wmsStationsPresentInBothAggregatedWMSAndCSVList = []

for csvName in csvStationsList:
    for key in wmsAggregatedStationsList:
        count += 1
        if(csvName == key):
            wmsStationsPresentInBothAggregatedWMSAndCSVList.append(wmsAggregatedStationsList[key])
            break

print('total steps of', count)