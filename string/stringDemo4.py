name = input("enter name :")
print(name)
#amit
#97...
#97-65 =32
#97-32 - 65
upperName =""
for i in range(0,len(name)):
    #print(name[i]) # a ,b
    #print(ord(name[i])) #97 #98
    #print(ord(name[i])-32) #65 66
    x = ord(name[i])-32 # A B
    #print(x)
    #print(chr(x))
    #"" = ""+"A" ="AB"
    upperName = upperName+chr(x)

print(upperName)    