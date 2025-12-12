#{1:1,2:2,3:3,4:4,5:5}

data = {}

for i in range(1,6):
    data[i] = i
print(data)    

#dict comr = {key:value for loop -->return --->key:value}
data1 = {i:i for i in range(1,6)}
print(data1)

#{1:1,2:4,3:9,4:16,5:25}

data2 = {i:i**2 for i in range(1,6)}
print(data2)