data = {100,20,30,401,90,18,30}
print(data)
print(type(data))

#set data acces..
#data[0] #TypeError: 'set' object is not subscriptable

# for i in data:
#     print(i)

#set data add..
data.add(1000)
print(data)

data.update({98,77,87,76,90,65,43})
print(data)

#remove data from set
#data.remove(401)
#data.remove(4001) #KeyError: 4001
#data.discard(4001) # it will not check membership
removedELm = data.pop()
print("remving...",removedELm)
print(data)