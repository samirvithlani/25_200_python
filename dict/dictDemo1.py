#empty dict
# data = {} #empty dict
# print(data)
# print(type(data))

#key:value
data = {"amit":23,"sumit":25,"raj":27,"kunal":22}
print(data)
#dict single data

print(data["amit"]) #it will return value of amit if key is not avaialble it will throw exception / error
print(data.get("kuna")) #it will return None if key is not presnt..

#get all keys
k = data.keys() #it will return an object of keys
print(k)
print(list(k)) #type cast keys object to list

v = data.values() ##it will return an object of keys
print(v)


#[('amit', 23), ('sumit', 25), ('raj', 27), ('kunal', 22)]
kv = data.items()
print(kv)

for i,j in data.items():
    print(i,"-",j)
