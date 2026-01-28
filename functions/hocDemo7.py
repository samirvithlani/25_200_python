def goa(name):
    print(f"{name} is going goa")
    return 45000

def kashmir(name):
    print(f"{name} is going kashmir")    
    return 60000

def tour(fn):
    amount = fn(name)
    print("amount = ",amount)

name = input("enter name :")    
tour(goa)