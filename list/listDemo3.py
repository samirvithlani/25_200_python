users = ["amit","sumit","ajay","raj","parth","kunal","neha"]
print(users)
removedElm = users.pop() #it will remove last element of list and also return it
print("remvoving...",removedElm)
print(users)

removedElm = users.pop(2) # 2 is index 
print("removing...",removedElm)
print(users)

# users.remove("parth") #r->None #ValueError: list.remove(x): x not in list

#solu..
name = "Parth"
#if "Parth" in users:
if name in users:
    users.remove(name) #elemrnt
else:
    print("element is not present..")    
print(users)