#create list of 1 to 5 using range loop

#trad way ...

data =[]
for i in range(1,6):
    data.append(i)

print(data)    

#comprehension
#both variable i must be same
#[i] == data1.append(i)
#[i for i in range(1,6)] --> 1,2,3,4,5 --> starring i -->
#[i] [for i in...] varibale name is i and it should be same
data1 = [i for i in range(1,6)]
print(data1)