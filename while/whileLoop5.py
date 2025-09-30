#check no is armstrong or not
#153 -->1 5 3
#1**3 -1 + 5**3 + 125 + 3**3 + 27 -- 1+125+27 = 153


no = int(input("enter no :"))
temp = no
sum =0
while no >0:
    rem = no % 10
    sum = sum + rem**3
    no = no //10


if sum == temp:
    print("no is armstrong no")    
else:    
    print("no is not armstrong no")    