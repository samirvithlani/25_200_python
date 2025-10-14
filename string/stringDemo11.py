data = "java is programming lang"

#ind = data.index("i") #ValueError: substring not found
ind = data.index("i",7) #boundries
print("index = ",ind)


ind2 =data.find("z") #if sub string is not present it will return -1
print("index2 = ",ind2)
