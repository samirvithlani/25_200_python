users = ["amit","sumit","ajay","raj","parth","kunal","neha"]
print(users)

name = input("ENter name to delete::")

#find index of given name
ind = -1
if name in users:
    ind=users.index(name)
    users.pop(ind)
else:
    print("user not found...")
print(users)    