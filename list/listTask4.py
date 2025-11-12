users = ["amit","sumit","ajay","raj","parth","kunal","neha"]
#name len >4 new list add

user2 =[]

for i in users:
    #amit 4 sumit . . 
    if len(i)>4:
        user2.append(i)
print(user2)        