file = open("names.txt","r")
c = input("enter char")
for i in file.readlines():
    if i.lower().startswith(c):
        print(i)


#
file2 = open("names.txt","r")        
filtFile = open("filtnames.txt","w")

for i in file2.readlines():
   if len(i.strip())>4:
        filtFile.write(i)
        