'''

//ini...;condi; increment
for(i=1;i<=10;i++){
    
    body...
}

'''

#range function... member ship operator....

#i=1 1 to 10 True

#range(1,10) --1 starts -- 9 default increment +1
for i in range(1,10):
    print(i,end=" ")

print()
#range(11) == it will starts from 0 and end to 10
for i in range(11):
    print(i,end=" ")    

print()

#range(1,20,2) starts from 1 end to 19 and increment by +2
for i in range(1,20,2):
    print(i,end=" ")


print()

for i in range(10,0,-1):
    print(i,end=" ")
    