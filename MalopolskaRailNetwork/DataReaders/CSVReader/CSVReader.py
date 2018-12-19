import csv

path = r'C:\Users\Dell\source\repos\MalopolskaRailNetwork\MalopolskaRailNetwork\InputFiles\StationsLocations.csv'

csvStationsList = []

with open(path, encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for row in csvReader:
        csvStationsList.append(row[4])

    #remove header from the list
    csvStationsList.remove('NAZWA')