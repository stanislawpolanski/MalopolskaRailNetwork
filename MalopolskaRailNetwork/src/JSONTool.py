import jsonpickle

def JSONSerialize(object, path):
    with open(path, 'w') as f:
        jsonObject = jsonpickle.encode(object)
        f.write(jsonObject)

def JSONDeserialize(path):
    with open(path) as f:
       jsonString = f.read()
       obj = jsonpickle.decode(jsonString)
    return obj

def test():
    print('test')