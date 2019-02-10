import DataReaders.wwwReaders.wwwReader as SourceOfRollingStock
RawRollingStock = SourceOfRollingStock.returnRollingStockList()

RollingStock_Dataset = []

for r in RawRollingStock:
    car = dict()
    car['Id'] = r['Id']
    car['OwnerId'] = r['OwnerId']
    car['Name'] = r['Name']

    RollingStock_Dataset.append(car)

def ReturnRollingStockDataset():
    return RollingStock_Dataset