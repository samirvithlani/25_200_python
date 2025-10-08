name= input("enter name :")
upperName = ""
#amit - 97 -121
for i in range(0,len(name)):
    #Amit -65
    if ord(name[i])>=65 and ord(name[i])<=91:
        x = ord(name[i])+32
        upperName = upperName + chr(x)
    else:
        upperName = upperName + name[i]    

print(upperName)        
        
#lower
#AMIT  - amit