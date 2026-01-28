def goa(name):
    print(f"{name} is going goa")

def kashmir(name):
    print(f"{name} is going kashmir")


def tour(fn):
    fn(name) #goa || kashmir

name = input("enter your name :")
tour(kashmir)    

    