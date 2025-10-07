name = "royal"
print(name)
print(name[0]) #
print(name[1]) #
print(name[2]) #

#immutable..
# name[0] ="R" #TypeError: 'str' object does not support item assignment
# print(name)
print("--------------")
data = "ahmedabad is beautiful city"
#length find...
#len function
l = len(data)
print("length of data = ",l)
# for i in range(0,l):
#     print(data[i])

# for i in range(0,len(data)):
#     print(data[i],end="")

for i in range(len(data)):
    print(data[i],end="")

#foreach loop
print()
for i in data:    
    print(i,end="")