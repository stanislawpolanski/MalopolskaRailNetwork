import Reports.Datasets.Railways_Dataset as Source_Railways
import Reports.Datasets.RailwayUnits_Dataset as Source_RailwayUnits
import Reports.Datasets.Stations_Dataset as Source_Stations

Railways_Geometries = Source_Railways.ReturnGeometriesPartialDataset()
RailwayUnits_Geometries = Source_RailwayUnits.ReturnGeometriesPartialDataset()
Stations_Geometries = Source_Stations.ReturnGeometriesPartialDataset()

Geometries_Dataset = RailwayUnits_Geometries + Railways_Geometries + Stations_Geometries
