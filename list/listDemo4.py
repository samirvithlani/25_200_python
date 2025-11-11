users = ["amit","sumit","ajay","raj","parth","kunal","neha"]
print(users)

#index-->
# name  = "raja" #find index of sumit
# ind = users.index(name) #->Index ->int #ValueError: 'raja' is not in list


#soln first check if element is present in list then find index
name = "neha"
ind = -1

if name in users:
    ind = users.index(name)
    
    

print("index of name = ",ind)
print(f"index of {name} = {ind}")