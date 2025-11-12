shapes = ["square","triangle","circle","square","rectangle","circle","dimond"]
uniqueList = []

#i = square
#i = triangle
#i  =square
for i in shapes:
    # "square" not in [] False
    if i not in uniqueList:
        uniqueList.append(i) #square ,

print(uniqueList)        