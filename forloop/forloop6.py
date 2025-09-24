#fibonacci series
#0 1 1 2 3 5 8  13 21..
#) + 1 = 1
# 1 + 1 =2
# 2 + 1 =3

#hint declare 2 var like a =0 , b = 1
#need to sum and swap

a = 0
b = 1

#0 1 2 3 5 8  13 21..
#0 +  1
print(a,end=" ") #0
print(b,end=" ") #1
for i in range(1,10):
    c = a + b # 0 + 1 = 1 # c = 1+ 1 =2 # c = 1 + 2 =3 # c = 2 + 3 =5
    # c= 1 a = 0 b=1
    # c = 2 a = 1 b =1
    # c = 3 a =1 b =2
    print(c,end=" ") #1 2 3 5
    #a = 1
    #a = 1
    #a = 2
    a = b
    #b = 1
    #b =2
    #b =3
    b = c
    
    
    
    
    
