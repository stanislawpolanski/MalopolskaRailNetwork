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
+ AnalysisShapely.RunAndSerializeIntersectionOfStationsAndUnits (that takes much time) - there's a product after that stage
+ AnalysisShapely.LoadIntersectedStations (product = stations with units)
+ Aggregators.StationsWithUnitsAggregator (stations with units aggregated by locations)
+ Aggregators.StationsWithUnitsAggregator (stations with units aggregated by locations - also a product) - this one abandons LHS stations
+ Analysis.IntersectStationsWithUnitsAggregatedAndCSV (extract final stations in the region)
+ Analysis.IntersectStationsWithUnitsAggregatedAndCSV_NoLHS (extract final stations in the region) - this is used for further analysis
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
Analysis.IntersectWMSWithWWW.IntersectRailwaysFromWMSWithWWW (railways from WWW enriched with lacking railways from WMS - LHS is present in the WWW DB so there's no need to skip it here)
Analysis.IntersectWMSWithWWW.IntersectStationsFromWMSWithWWW_NoLHS (stations from WWW enriched with lacking stations from WMS) - lhs data from WWW skipped in this analysis
Reports.ReportMergedRailways
Reports.ReportMergedStations
Reports.ReportMergedRailwaysWithStations
## CSV QGIS extract
+ DataReaders.CSVReader.CSVReader
