# user can apply for visa if he/she has aadharcard or paancard and he/she must have passport
# user age must grt > 1 year

aadharcard = True
pancard =  False
passport =True
age =0

if (aadharcard == True or pancard == True) and passport == True and age>=1:
    print("you will get visa")
else:
    print("you will not get visa")    
