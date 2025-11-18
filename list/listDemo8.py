data = [[1,2,3],[4,5,6],[7,8,9]]    
print(data)

print(data[0])
print(data[1])
print(data[2])

#8
print(data[2][1])
#6
print(data[1][2])

# data[0][2]=30
# print(data)

#itrate 
#range

#i =0
#i =1
#i =2
for i in range(0,len(data)):
    #print(data[i]) #[1,2,3]
    
    #j=0
    for j in range(0,len(data[i])):
        #data[0][0] #data[0][1] data[0][2] /n
        #data[1][0] #data[1][1] data[1][2]
        #data[2][0] #data[2][1] data[2][2]
        print(data[i][j],end=" ")
    
    print() #/n        