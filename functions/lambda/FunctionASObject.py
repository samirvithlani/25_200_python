def test():
    print("tets function called...")
    return 100

# x = test() #function calling part...
# print("x = ",x)

# test  #no error
x = test #test function address == x
print("x  =",x)
x() #test