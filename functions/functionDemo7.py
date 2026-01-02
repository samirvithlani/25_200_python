#keyword argument functions

def getUserData(name,email,age,salary):
    print(f"Name = {name}")
    print(f"Email = {email}")
    print(f"Age = {age}")
    print(f"Salary = {salary}")


#getUserData("raj","raj@gmail.com",23,45000)    
#getUserData("raj@gmail.com",23,45000,"raj")    

#keyword argument
#getUserData(name="raj",salary=45000,email="raj@gmail.com",age=23)
#getUserData(name="raj",salary=45000,email="raj@gmail.com",23) #all param must be keyword