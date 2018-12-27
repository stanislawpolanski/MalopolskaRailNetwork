## How's the progress
 For the up-to-date status see: [https://github.com/stanislawpolanski/MalopolskaRailNetwork/blob/master/MalopolskaRailNetwork/Documents/RoadMap.md](https://github.com/stanislawpolanski/MalopolskaRailNetwork/blob/master/MalopolskaRailNetwork/Documents/RoadMap.md)
 ## The aim of the project
This project is developed for needs of [Małopolskie stacje kolejowe website](http://stacje.cba.pl/). From the list of the stations and list of geographic coordinates stations it will come to full list of stations in Małopolska region (with associations to rail lines). It uses following packages.
### Dependencies
+ [numpy](http://www.numpy.org/)
+ [shapely](https://pypi.org/project/Shapely/)
+ [matplotlib](https://matplotlib.org/index.html)
+ [jsonpickle](https://jsonpickle.github.io/)
## Modules
+ Aggregators - One station in a source file may be listed few times. This module aggregates redundant stations occurences into one.
+ Analysis - Analysis using text data.
+ AnalysisShapely - geographic analysis.
+ 