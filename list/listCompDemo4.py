names = ["amit","sumit","kunal","jay","raj","parth"]
upperNames =[] #empty list..
#convert every name to upperCase and add it to new list

#trad approch..
for i in names:
    upperNames.append(i.upper())
print(upperNames)    

#compre

upperNames1 = [i.upper() for i in names]
print(upperNames1)
