#Map : it is use for tranform any iterable data

users = ["raj","parth","amit","sumit","neha"]

#loop
upperUser =[]
for i in users:
    upperUser.append(i.upper())

print(upperUser)    

#comprehension..
upperUser1 = [i.upper() for i in users]
print(upperUser1)

#map
upperUser2 = map(lambda x:x.upper(),users)
print(list(upperUser2))

#marks
marks = [23,24,33,45,32]
#+5
marks1 = map(lambda x:x+5,marks)
print(list(marks1))

sales = [800,700,600,1200,700,755] 
# 30 % costing remove it and give gorss profit
# sales1 = map(lambda x:x>700,sales)
# print(list(sales1))

sales1=filter(lambda x:x>700,sales)
print(list(sales1))

users = ["raj","parth","amit","naman","sumit","neha","bob"]
#return all palindorome names
#return all names whose len > 4
# return all names ends with a or i
# return all names starts with s