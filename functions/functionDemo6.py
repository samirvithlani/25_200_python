def checkLength(data):
    if len(data)==0:
        return False
    else:
        return True


if checkLength(""):
    print("len is fine")    
else:
    print("len is not valid...")    