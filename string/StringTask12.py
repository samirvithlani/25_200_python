name = "java"
ind = -1
char = "a"

#
for i in range(0,len(name)):
    #  j == a -- False
    #  a == a -- True
    #  v ==a == False
    #  a == a = True
    if name[i] == char:
        #1,3
        ind = i
        break    
print("found index = ",ind)    