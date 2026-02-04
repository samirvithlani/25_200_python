name = "amit"
age=23
city="Ahmedabad"
file = open("user.txt","a")

file.write(f"Name = {name}")
file.write(f"\nAge = {age}")
file.write(f"\nCity = {city}")

file.close()

