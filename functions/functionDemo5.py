#function returning Bool

#if data contain space it is not valid or it is valid
def isValid(data):
    if " "in data:
        return False
    else:
        return True

# flag = isValid("ajay jadeja")    
# print(flag)

#note if function is returing bool value [True,false ] we can use that function in if block direclty...
#if isValid returns true if part will exceute..or else part will execute

if isValid("Raj"):
    print("name is valid.")    
else:
    print("name is not valid..")    