# create a function pass list to funciton
# and find max element from list


def findMax(data):
    max = data[0]
    for i in data:
        if i >max:
            max =i
    return max        
    

ans = findMax([10,20,30,40,400,65])    
print(ans)


# create funciton pass list to funciton
# and check all elements in list are int or not if all are int return true or false

# def checkElm(data):
#     flag = True
#     for i in data:
#         if type(i)!= int:
#             flag = False
#             break
#     return flag    


def checkElm(data):
    flag = True
    for i in data:
       if not isinstance(i,int):
            flag = False
            break
    return flag    


ans = checkElm([10,200,56,78])    
print("ams = ",ans)