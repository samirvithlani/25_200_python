names = ["amit","sumit","kunal","jay","raj","parth","ajay","anurag"]

#name starts with a -->[]
nameswitha =[]

for i in names:
    if i.startswith("a"):
        nameswitha.append(i)

print(nameswitha)        

#compre

nameswitha1 = [i for i in names if i.startswith("a")]
print(nameswitha1)