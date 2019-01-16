#this list contains list stations that meets all the condintions:
# - former PLK
# - exist in the WWW DB
# - do not exist in the WMS (destroyed)

nonExistingStations = ["Płaza", "Nowy Targ Fabryczny", "Ludźmierz", "Czarny Dunajec", "Rogoźnik Podhalański", "Podczerwone", "Skawce"]

def returnList():
    return nonExistingStations