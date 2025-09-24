##get 2 number from user no1 measns startp and ending point
#eg 10 20 -->10, 11,12
#print only even no bw them...

sp = int(input("enter starting point :"))
ep = int(input("enter starting point :"))


for  i in range(sp,ep+1):
    if i %2==0:
        print(i)