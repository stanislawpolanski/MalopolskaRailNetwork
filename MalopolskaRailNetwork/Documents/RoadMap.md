# Project roadmap
The roadmap.
## Reading data
+ [x] Read three files:
  + [x] WMS_SILK_linie_kolejowe.xml (Railways)
  + [x] WMS_SILK_stacje_przystanki.xml (Stations)
  + [x] WMS_SILK_zaklady.xml (Railway Units)
+ [x] Serialize to JSON
  + [x] Serializer scripts
  + [x] Deserializer scripts
+ [x] aggregate stations locations info
## Integration with stacje.cba.pl
+ [x] Download data to XML
+ [x] Reading stacje.cba.pl data into Python
  + [x] reading stations
  + [x] reading railways
  + [x] reading owners
  + [x] reading stations to railways
+ [x] Extract stations in the Małopolska region using csv file
  + [x] read csv file
  + [x] intersect csv with wms file
  + [x] create output
+ [x] Extract railways in the Małopolska region using intersected wms/csv file
  + [x] extract railways in the region from stations wms/csv file
  + [x] intersect those railways with wms railways file
  + [x] create output
+ [ ] intersect data with railway units (shapely?)
  + [x] stations to points (go with raw stations, as they have no aggregated geographic info)
  + [x] railway units to polygons
  + [x] plot railways and stations on one image
  + [x] intersection to list (station -> railway unit)
    + [x] intersect data
    + [x] save data
  + [ ] aggregate stations info with units by geographic locations
  + [ ] create output (stations with railway units)
+ [ ] Update db file with stations from csv/wms file
  + [ ] create extended db file
    + [ ] add to the db file new columns
  + [ ] intersect db file with wms/csv stations
  + [ ] intersect db file wms/csv railways
+ [ ] Update database file
  + [ ] Create output XML for integration with database
  + [ ] Fill the output file with lacking railways
  + [ ] Fill the output file with lacking stations
+ [ ] Create realtions in output file (stations to railways)
+ [ ] merge with stacje.cba.pl
  + [ ] create backup
  + [ ] update
## Graph analysis
+ [ ] writing sets to graph
+ [ ] Design analysis
## Project evaluation
+ [ ] Update readme
+ [ ] Conclusions