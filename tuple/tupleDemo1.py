#empty tuple

# data = () #emplty tuple
# print(data)
# print(f"type of data = {type(data)}")
# print(f"type of data = {type(data).__name__}")


users = ("amit","sumit","ajay","parth","sumit")
print(users)
print(users[0])
print(len(users))

#using range

# for i in range(0,len(users)):
#     print(users[i])

# for i in users:
#     print(i)

#users[0] ="Amit" #ypeError: 'tuple' object does not support item assignment
print(users)

cnt =users.count("sumit")
print("count = ",cnt)

ind = users.index("parth")
print("index",ind)