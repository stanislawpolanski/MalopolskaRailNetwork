#Aggregators...
import Aggregators.WMSStationsAggregator
wmsAggregatedStationsList = Aggregators.WMSStationsAggregator.returnAggregatedStationsDict()
#DataReaders/CSVReader/CSVReader.py
import DataReaders.CSVReader.CSVReader
csvStationsList = DataReaders.CSVReader.CSVReader.returnCSVStationsList()

#now intersect both datasets, keep fields of wms stations
count = 0

wmsStationsPresentInBothAggregatedWMSAndCSVList = dict()

for csvName in csvStationsList:
    for key in wmsAggregatedStationsList:
        count += 1
        if(csvName == key):
            wmsStationsPresentInBothAggregatedWMSAndCSVList[key] = wmsAggregatedStationsList[key]
            break

#print('total steps of', count)

def returnWMSAggregatedStationsPresentInCSV():
    return wmsStationsPresentInBothAggregatedWMSAndCSVList