data = [1,2,3,44,56,77,89,111,234,567,89,90]
evenData =[]

#trad

for i in data:
    if i %2 ==0:
        evenData.append(i)

print(evenData)        

#comprehension

evenData1 = [i for i in data if i % 2 ==0]
print(evenData1)


