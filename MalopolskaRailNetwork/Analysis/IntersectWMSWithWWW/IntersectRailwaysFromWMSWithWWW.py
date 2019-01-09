#import wms railways
import Analysis.ExtractRailwaysNamesInTheRegion as wmsSource

wms = wmsSource.returnNamesAndNumbersOfTheRailwaysInTheRegionDict()

#import www railways
import DataReaders.wwwReaders.wwwReader as wwwSource

www = wwwSource.returnRailwayList()

#intersect


#return result
