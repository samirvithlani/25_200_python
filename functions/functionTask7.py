def getFullData(data1,data2):
    return set(data1+data2)

x = getFullData(["jay","raj","parth"],["amit","sumit","kunal","jay","parth"])
print(x)