# #param + return type
# def add(a,b):
#     return a + b

# ans = add(100,20)
# print("ans = ",ans)

#lambda version

#no need to write retuen keyword
x = lambda a,b : a+b
ans = x(1000,1)
print("ans = ",ans)

#stirng param lambda..

x1 = lambda fname,lname : fname+" "+lname
fullName = x1("virat","kohli")
print("fullname = ",fullName)