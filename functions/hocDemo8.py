def goa(name):
    print(f"{name} is going goa")
    return 45000

def kashmir(name):
    print(f"{name} is going kashmir")    
    return 60000

# def tour(fn):
#     amount = fn(name)
#     return amount

def tour(fn):
    return fn(name) #fn -->return tour-->

name = input("enter name :")    
finalAmount = tour(kashmir)
print("finalAmount  = ",finalAmount)