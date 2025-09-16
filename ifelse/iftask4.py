
# GET INPUT of AGE AND GENDER [male,female]

# if AGE<12 ticket price will be 50
# if gender is female and  30
# or else price will be 100

age = int(input("enter age :"))
gender = input("enter gender :")


if age>12:
    print("age > 12")
    if gender=="female":
        print("your gender is female and ticekt price will be 30")
    else:
        print("your gender is male and ticket price will be 100")    
else:
    print("you are childern : and your ticket price will be 30")        
        