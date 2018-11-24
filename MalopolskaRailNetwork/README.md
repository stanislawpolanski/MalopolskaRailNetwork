﻿## The aim of the project
This project is developed for needs of [Małopolskie stacje kolejowe website](http://stacje.cba.pl/). From the list of the stations and list of geographic coordinates stations it will come to full list of stations in Małopolska region (with associations to rail lines).
## Raw data
+  META_GRANICE_ZAKLADOW.xml
+  META_LINES.xml
+  WMS_SILK_linie_kolejowe.xml
+  WMS_SILK_stacje_przystanki.xml
+  WMS_SILK_zaklady.xml
## Input data
+ /InputFiles/StationsLocations.csv - list of stations with their locations,
+ /InputFiles/WykazPosterunkow.pdf - pdf with stations and their rail lines assignments
## Analysis design
### Data integration
#### Reading data
The first step is to succesfully load all the data. Both files will be loaded and saved seperately into arrays into:

/LoadedData
#### Merging datasets
Both datasets will be merged
## Result