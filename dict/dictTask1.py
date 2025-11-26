data ={}

while True:
    name = input("Enter Name :")
    if name == "exit":
        break
    age = int(input("Enter Age:"))
    data[name]= age

print(data)    
        