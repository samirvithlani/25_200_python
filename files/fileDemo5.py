#1st way

# file = open("demo1.txt","r")
# #data = file.read()
# data = file.read(10)
# print(data)


#2nd way
# file = open("th.txt","r")
# x =file.readline()
# print(x)

# file = open("th.txt","r")
# line =0
# while True:
#     x = file.readline()
#     print(x,end="")
#     line+=1
#     if not x:
#         break

# print("no of line = ",line)    


#3rd way

# file = open("th.txt","r")

# for i in file:
#     print(i,end="")

#4th way

file = open("th.txt","r")

# x = file.readlines()
# print(x)
# for i in x:
#     print(i,end="")

for i in file.readlines():
    print(i,end="")