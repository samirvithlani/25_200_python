def getData(**kwargs):
    return list(kwargs.keys())


x =getData(name="amit",age=23,city="ahmedabad",salary=32000)
print(x)

#give all keys as list in return
#["name","age","city,"salary"]


# def getBill(**kwargs):
#     total = 0
#     for v in kwargs.values():
#         total = total+v
#     return total    

def getBill(**kwargs):
    total =0
    dis = kwargs.get("discount")  
    
    for k,v in kwargs.items():
        if k!="discount":
            total+=v
    total = total - (total*dis)/100
    return total
    


x = getBill(tea=40,coffee=60,snacks = 100,discount=10)
print(x) #print total in x


# def myMarks(**marks):
#     total=0
#     for m in marks.values():
#         total+=m
#     return total    

# total =myMarks(eng=78,maths=82,science=86,phy=77)
# print(total)


def myMarks(**marks):
    heighest= list(marks.keys())[0]
    for k,v in marks.items():
        if v>marks[heighest]:
            heighest = k
    return heighest        
    
    

heighest = myMarks(eng=78,maths=82,science=86,phy=77)
print(heighest)
