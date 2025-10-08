#find no spaces in sent..
#i love my country

sent = "i love my country and my"
count=0
for i in sent:
    if i ==" ":
        count+=1

print("no of space in sent = ",count+1)        