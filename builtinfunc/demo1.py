fruits = ["apple","banana","mango"]

# for i in range(len(fruits)):
#     print(i,fruits[i])

#foreach 
# for i in fruits:
#     print(i)

#foreach with index..

for i,f in enumerate(fruits):
    print(i,f)
    
#zip
names = ["raj","jay","parth"]    
score =[90,78,76]

#0 -->0
for i,j in zip(names,score):
    print(i,"-",j)


names = ["raj","jay","parth"]    
score =[90,78,76]
age=[10,20,30]    

for i,j,k in zip(names,score,age):
    print(i,j,k)


    