#sorted
nums = [5,1,3,2]
x = sorted(nums)
print(x)

names = ["raj","ajay","parth","Kunal","neha","seema","perth"]
x1 = sorted(names)
print(x1)
x2 = sorted(names,reverse=True)
print(x2)
#by len
x3 = sorted(names,key=len)
print(x3)
x3 = sorted(names,key=len,reverse=True)
print(x3)