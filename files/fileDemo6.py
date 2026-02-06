file = open("demo1.txt","r")

data=[]
while True:
    x = file.readline()
    if not x:
        break
    word = x.split(" ") #["" "" ""]
    for i in word:
        i = i.strip()
        if i ==i[::-1]:
            data.append(i)
    
print(data)        