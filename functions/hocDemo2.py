def science():
    print("admission in science..")

def comm():
    print("admission in comm..")

def arts():
    print("admission in arts..")        



def admission(fun):
    print("admission function called....")
    #fun == science,comm,arts
    fun() #sci,commarts


#if esle
pers = 74
if pers>=80:
    admission(science)    
elif pers>=70:
    admission(comm)
elif pers>=60:
    admission(arts)
else:
    print("no admission..")    
        
    