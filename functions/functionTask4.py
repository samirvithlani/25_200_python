# def convertUpper(data):
#     upperList =[]
#     for i in data:
#         upperList.append(i.upper())
    
#     return upperList    

def convertUpper(data):
    return [i.upper() for i in data]


x = convertUpper(["raj","amit","kunal","jay"])
print(x)#["RAJ","AMIT","KUNAL","JAY"]