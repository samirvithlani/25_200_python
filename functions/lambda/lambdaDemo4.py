# #if else with lambda

# def findMax(no1,no2):
#     if no1>no2:
#         return no1
#     else:
#         return no2

# ans = findMax(100,20)
# print("ans = ",ans)    

#lambda version

x = lambda no1,no2 : no1 if no1>no2 else no2
ans = x(100,20)
print("ans = ",ans)

#check stirng is palindrome or not using lambda function
#hint using slicing..

#x = lambda name: logic

x = lambda name: True if name==name[::-1] else False
ans = x("namana")
print("ans = ",ans)


#create lambda function and accept number as argumnet check if no is pos return "positive" else "Neg"

x1 = lambda no : "pos" if no >0 else "Neg"
ans = x1(-100)
print("ans = ",ans)