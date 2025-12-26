#return type function

# def add(a,b):
#     print("add function called..")
#     c = a + b #30
#     return c #always value return #30

# ans = add(10,20)
# print("ans = ",ans)


# def add(a,b):
#     print("add function called..")
#     return a+b #10 + 20 = 30
    

# ans = add(10,20)
# print("ans = ",ans)

#if any function is returning any value you can directly call in print function


def add(a,b):
    print("add function called..")
    return a + b

# ans = add(10,20)
# print("ans = ",ans)

#note: if funciton is not returning any value and we print like below it will print None
print("ans = ",add(10,20))