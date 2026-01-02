def getAllKeys(data):
    return list(data.keys())

users = {"raj":100,"parth":200,"jay":20}
x = getAllKeys(users)
print(x)


def getAllValues(data):
    return list(data.values())

users = {"raj":100,"parth":200,"jay":20}
x = getAllValues(users)
print(x)