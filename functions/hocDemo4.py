def science(name):
    print(f"Hello {name} welcome to science")

def comm(name):
    print(f"Hello {name} welcome to comm")

def arts(name):
    print(f"Hello {name} welcome to arts")        


def admission(fun,name):#science
    print("admission called...")    
    fun(name) # sc,com,arts...


pers = 81
name = "raj"

if pers>=80:
    admission(science,name)
elif pers>=70:
    admission(comm,name)    
elif pers>=60:
    admission(arts,name)    
else:
    print("no admission...")    