def science(name):
    print(f"Hello {name} welcome to science")

def comm(name):
    print(f"Hello {name} welcome to comm")

def arts(name):
    print(f"Hello {name} welcome to arts")        


def admission(fun):#science
    print("admission called...")    
    fun("raj") # sc,com,arts...

pers = 81

if pers>=80:
    admission(science)
elif pers>=70:
    admission(comm)    
elif pers>=60:
    admission(arts)    
else:
    print("no admission...")    