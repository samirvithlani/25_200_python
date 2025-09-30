#reverse the number 
#123 -->output will be 321

no = int(input("enter no :"))
rev = 0
#
while no >0:
    #123% 10 =3
    #12 % 10 2
    #1 % 10 1
    rem = no % 10
    #rev = 0*10 + 3 = rev = 3
    #3 = 3 * 10 + 2 = 32
    #32 = 32*10 + 1 = 321
    rev = rev *10+rem
    #12
    #1
    #0
    no = no //10

print("sum =",rev)    
    