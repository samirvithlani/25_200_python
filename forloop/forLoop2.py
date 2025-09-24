#get 2 number from user no1 measns startp and ending point
#eg 10 20 -->10, 11,12
#print sum of all number

sp = int(input("enter starting point :"))
ep = int(input("enter starting point :"))

sum =0
#1,10
for i in range(sp,ep+1):
    #0 = 0 + 1 sum= 1
    #1 = 1 + 2 sum =3
    #3 = 3 + 3 sum =6
    #>...
    sum = sum + i
    print(i)

print(f"sum = {sum}")    
print("sum = ",sum)
