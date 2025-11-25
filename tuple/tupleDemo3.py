#how to change data in tuple

marks = (78,89,76,56,90,92)
print(marks)
#convert tuple to list..
marksList = list(marks)
#print(marksList)
#change in list
marksList[3]=66
#again convert it to new tuple object..
marks = tuple(marksList)
print(marks)

