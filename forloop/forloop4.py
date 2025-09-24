#take number from user and print table in below format
#5
#5 * 1 = 5
#5 * 2 = 10
#...

no = int(input("enter no to print table :"))

for i in range(1,11):
    #print(f"{no} * {i} = {no*i}")
    print(no," * ",i," = ",no*i)