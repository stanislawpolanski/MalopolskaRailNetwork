# Project roadmap
The roadmap will be published after finish of the design.
+ [x] Read three files:
  + [x] WMS_SILK_linie_kolejowe.xml (Railways)
  + [x] WMS_SILK_stacje_przystanki.xml (Stations)
  + [x] WMS_SILK_zaklady.xml (Railway Units)
+ [x] Serialize to JSON
  + [x] Serializer scripts
  + [x] Deserializer scripts
+ [ ] establishing relationship between lines & stations
  + [ ] aggregate stations locations info (by lines they belong to)
  + [ ] join stations to lines
+ [ ] writing stations to SQL
+ [ ] writing sets to graph
+ [ ] Graph analysis