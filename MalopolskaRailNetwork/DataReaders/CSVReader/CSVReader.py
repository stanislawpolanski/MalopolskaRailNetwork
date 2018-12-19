import csv

path = r'C:\Users\Dell\source\repos\MalopolskaRailNetwork\MalopolskaRailNetwork\InputFiles\StationsLocations.csv'

with open(path, encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for row in csvReader:
        print(row)