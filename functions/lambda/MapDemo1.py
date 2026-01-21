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

