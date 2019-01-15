# Progress with datasets
## WMS datasets and further analysis
### Stations from WMS
+ DataReaders.StationsReader
+ Serializers.SerializeStations
+ Deserialisers.StationsDeserialize
+ Aggregators.WMSStationsAggregator (aggregation by location points)
+ Analysis.IntersectStationsFromWMSAggregatedAndCSV
+ AnalysisShapely.RawStationsToShapelyPoints
+ AnalysisShapely.IntersectionOfStationsWithUnits (that takes much time)
+ AnalysisShapely.RunAndSerializeIntersectionOfStationsAndUnits (that takes much time)
+ AnalysisShapely.LoadIntersectedStations (product = stations with units)
+ Aggregators.StationsWithUnitsAggregator (stations with units aggregated by locations - also a product)
+ Analysis.IntersectStationsWithUnitsAggregatedAndCSV (extract final stations in the region)
### Railways from WMS
+ DataReaders.RailwaysFromRailwaysReader
+ Serializers.SerializeRailways
+ Deserialisers.DeserializeRailways
+ Analysis.ExtractRailwaysNamesInTheRegion (from Analysis.IntersectStationsFromWMSAggregatedAndCSV)
### Railway units from WMS
+ DataReaders.RailwayUnitFromRailwaysUnitReader
+ Serializers.RailwayUnitsSerializer
+ Deserialisers.RailwayUnitsDeserialiser
+ AnalysisShapely.RailwayUnitsToShapelyPolygons
## WWW dataset - All datasets read simultaneusly
+ DataReaders.wwwReaders.stacjecbaplReader
### Data merge
Analysis.IntersectWMSWithWWW.IntersectRailwaysFromWMSWithWWW (railways from WWW enriched with lacking railways from WMS)
## CSV QGIS extract
+ DataReaders.CSVReader.CSVReader
