data = {"amit":23,"sumit":25,"raj":27,"kunal":22}
print(data)
#data.pop("raj") #if key is not present it willl throw error
removedValue = data.pop("raj") #if key is not present it willl throw error
print('removing...',removedValue)
print(data)


data = {"amit":23,"sumit":25,"raj":27,"kunal":22}
print(data)
#data.popitem()
removeItem = data.popitem()
print("removing...",removeItem)
print(data)


