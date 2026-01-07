# #*args
# def getUsers(*user):
#     print(user)


# getUsers("raj","jay","parth","amit")    

#kwargs
#kwrags is not keyword
#it will accept 0 to n argument
def employeeData(**kwargs):
    print(kwargs)

employeeData(name="raj",age=23,city="ahmedabad")    