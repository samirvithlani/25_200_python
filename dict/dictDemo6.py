data = {101:"Ahmedabad",102:"surat",103:"gandhinagr"}

#get all keys from dict..
k = data.keys()
print(k) #it will return an object
print(list(k)) #type cast..

v = data.values()
print(v)

#[(101, 'Ahmedabad'), (102, 'surat'), (103, 'gandhinagr')]
kv = data.items()
print(kv)


#i = key j =value
for i,j in data.items():
    print(i,"-",j)
