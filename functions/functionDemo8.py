# def getUsers(name):
#     print(name)

# getUsers("raj")    

#args arugument variables...
#args is not a keywors
#args can accept min 0 to max n argument
def getUsers(*args):
    print(args)

#getUsers("raj","parth","amit")    
getUsers()

#note 1:
# def getEmployees(*emps,x):
#     print(emps)
#     print(x)
    
# getEmployees("mark","bill","musk")    

#solution 1    
#args must be last argument
def getEmployees(x,*emps):
    print(emps)
    print(x)
    
getEmployees("mark","bill","musk")    

#solution 2
#you can pass keyword argument
def getEmployees(*emps,x,y):
    print(emps)
    print(x)
    
getEmployees("mark","bill","abcd", x = "musk",y="warran")    