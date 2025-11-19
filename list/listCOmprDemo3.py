data = [1,2,3,4,5]
#do sqaure and add it into a new list
sqlist =[]
#trad

for i in data:
    sqlist.append(i**2)
print(sqlist)    

#compre

sqlist2 = [i**2 for i in data]
print(sqlist2)
    
