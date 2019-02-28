# Final dataset agreement
## Assumptions
Final dataset should include both railways and stations and their relations. It will be three datasets. On of stations (with locations - those will represent relationships between stations and railways), railway units and another of railways. Abbreviations:
+ PK - primary key
+ FK - foreign key
### Geometries
+ Id - key
+ Value - geometries
### Railway units dataset
+ Id
+ Name
+ GeometriesId - FK to Geometries
### Railways dataset
Railways dataset will be stored as a list of dicts. Each dict will represent one railway. They keys will be following:
+ Id (inherited from DB key)
+ Name
+ Number
+ OwnerId (read from DB, new PLK OwnerId = 1)
+ GeometryId [optional] - FK to WMS geometry
### Stations dataset
List of dicts, param LocationPoints is a list of dicts with locations.
#### Structure of stations dataset
+ Id (inherited from StatDB key)
+ Name
+ OwnerId (read from DB, new PLK OwnerId = 1)
+ RailwayUnitId - FK to railway units
+ TypeOfAPoint (may be station, siding etc.)- FK to Types of a point table
+ LocationPoints[]
#### Structure of LocationPoints subset (relations to DB)
+ Id - PK
+ StationId - FK to Stations
+ GeometryId [optional] - FK to geometries
+ BeginningKmpost [optional] 
+ CentreKmpost
+ EndingKmpost [optional] 
+ RailwayId - FK to railways
#### Types of a point
+ Id - PK
+ AbbreviatedName - like PO, ST
### Owners dataset
+ Id - PK
+ Name
### Rolling stock dataset
+ Id - PK
+ OwnerId - FK to Owners
+ Name
