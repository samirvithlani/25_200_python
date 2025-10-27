#string[start:end:step]

#string[0:4:1] 0 include 4 exlude 1

text = "Python"
print(text[0:4])# 0-->3

#ommiting start or end
print(text[:4]) #start from 0 and 4
print(text[2:]) #starts from 2nd index and will go to end..

#negtive slicing
#P   Y   T   H   O   N
#0   1   2   3   4   5
#-6  -5  -4  -3  -2  -1

print(text[0])
print(text[-1])
print(text[-6])

#negative slicing:
print(text[-3:])
print(text[:-2])