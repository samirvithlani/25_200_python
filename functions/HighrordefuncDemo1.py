#hoc

def calling():
    print("calling function called...")
def texting():
    print("texting called........")    

def demo(a):
    print("demo function called..")
    #print(a) #100 java False [] calling
    #a == calling()
    a() #it will call calling function...

# demo(100)    
# demo("java")
# demo(False)
# demo([])
demo(calling)
demo(texting)