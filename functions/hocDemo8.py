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



#upi credicard, debitcar, netbankin
#2%  2.5         1          0.5

def payment(fn):
    pass

#amount=input 100
#charges = payment(upi)
#print() #2