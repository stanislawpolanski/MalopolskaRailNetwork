import Reports.Datasets.Railways_Dataset as Source_Railways
import Reports.Datasets.RailwayUnits_Dataset as Source_RailwayUnits
import Reports.Datasets.Stations_Dataset as Source_Stations

Railways_Geometries = Source_Railways.ReturnGeometriesPartialDataset()
RailwayUnits_Geometries = Source_RailwayUnits.ReturnGeometriesPartialDataset()
Stations_Geometries = Source_Stations.ReturnGeometriesPartialDataset()

for r in Railways_Geometries:
	r['Value'] = 'LINESTRING(' + r['Value'] + ')'

for u in RailwayUnits_Geometries:
	u['Value'] = 'MULTIPOLYGON(' + u['Value'] + ')'

for s in Stations_Geometries:
	s['Value'] = 'POINT(' + s['Value'] + ')'

Geometries_Dataset = RailwayUnits_Geometries + Railways_Geometries + Stations_Geometries

for row in Geometries_Dataset:
	row['Value'] = row['Value'].replace(',', '#')
	row['Value'] = row['Value'].replace(' ', ',')
	row['Value'] = row['Value'].replace('#', ' ')

import src.JSONTool as jst
path = 'C:\\Users\\Dell\\source\\repos\\MalopolskaRailNetwork\\MalopolskaRailNetwork\\Data\\DataSnapshots\\FinalDatasets\\Geometries_Dataset.json'

jst.JSONSerialize(Geometries_Dataset, path)
print("serialising done - geometries")