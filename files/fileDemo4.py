name = "amit"
age=23
city="Ahmedabad"
file = open("user.txt","a")

file.write(f"Name = {name}")
file.write(f"\nAge = {age}")
file.write(f"\nCity = {city}")

file.close()

#heading user data
data= {"name":"amir","age":23,"city":"Ahmedabad","salary":25000}

file = open("user1.txt","a")
file.write('User Data:\n')
for i,j in data.items():
    file.write(f"{i} = {j}\n")

file.close()    

data = {"Virat":[80,90,100],"Rohit":[90,89,120,78],"Pandya":[45,67,87]}    

#Virat
#match 1 score = 80
#match 2 score = 90
#match 3 score = 80

#Rohit

