#get 2 no from user and check which one is bigger and store into min and max
no1 = int(input("enter no 1 : "))
no2 = int(input("enter no 2 : "))
min = 0
max = 0

#12 >22 False
#50 >20 True
if no1 > no2:
    print("no1 is greater !!")
    max = no1 #max= 50
    min = no2 #min = 20
else:
    print("no2 is greater !!")    
    max = no2 #max = 22
    min = no1 #min = 12

print("min = ",min)    
print("max = ",max)
    

    