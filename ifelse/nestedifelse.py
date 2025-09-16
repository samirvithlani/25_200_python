#if 1 condition get sucess of faile on behalf of that condition we have to check another 
#condition called. nested ...
#if your have passs sec check
#they will check your ticket...

age = int(input("enter age :"))

if age >= 18:
    print("user is eligible for voating...")
    if age>21:
        print("user is eligble for marrige ...")
    else:
        print("user is not eligble for marrige...")
    
else:
    print("user is not eligbile for voating...") 
    
    if age>16:
        print("user is eligible for 2 wheeler lic...")   
    else:
        print("stay at home !!")    
    