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
+ [ ] Extract stations in the Małopolska region using csv file
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