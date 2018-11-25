## The aim of the project
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
The first step is to succesfully load all the data. Stations files will be loaded into arrays into (depends on time of reading of data):

+ /DataRead

This script will be stored there:
+ src/DataReaders/StationsReader.py
+ src/DataReaders/LinesFromStationsReader.py (from stations file!)
+ src/DataReaders/LinesFromLinesReader.py
#### Merging datasets
Both datasets will be merged as a n:n relationship.
#### Print out as an SQL
For further processing it will be printed out as an SQL with three tables:
+ Stations
+ RailLines
+ StationsToRaiLines
## Result