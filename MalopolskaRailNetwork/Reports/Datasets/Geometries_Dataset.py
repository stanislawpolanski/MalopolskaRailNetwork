import Reports.Datasets.Railways_Dataset as Source_Railways
import Reports.Datasets.RailwayUnits_Dataset as Source_RailwayUnits
import Reports.Datasets.Stations_Dataset as Source_Stations

Railways_Geometries = Source_Railways.ReturnGeometriesPartialDataset()
RailwayUnits_Geometries = Source_RailwayUnits.ReturnGeometriesPartialDataset()
Stations_Geometries = Source_Stations.ReturnGeometriesPartialDataset()

for r in Railways_Geometries:
	r['GeometryType'] = 'LineString'

for u in RailwayUnits_Geometries:
	u['GeometryType'] = 'MultiPolygon'

for s in Stations_Geometries:
	s['GeometryType'] = 'Point'

Geometries_Dataset = RailwayUnits_Geometries + Railways_Geometries + Stations_Geometries

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\Geometries_Dataset.json'

jst.JSONSerialize(Geometries_Dataset, path)
print("serialising done")