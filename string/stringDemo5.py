name= input("enter name :")
upperName = ""
#amit - 97 -121
for i in range(0,len(name)):
    #Amit -65
    if ord(name[i])>=97 and ord(name[i])<=121:
        x = ord(name[i])-32
        upperName = upperName + chr(x)
    else:
        upperName = upperName + name[i]    

print(upperName)        
        
        