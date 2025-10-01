no1 = int(input("enter no 1:"))
no2 = int(input("enter no 2:"))

max =0
if no1>no2:
    max = no1
else:
    max = no2    

#15
lcm =0 #0

while True:
    
    if max % no1 ==0 and max %no2 ==0:
        lcm = max
        break
    max+=1

print("lcm  =",lcm)    