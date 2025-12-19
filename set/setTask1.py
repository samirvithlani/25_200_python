# Task:
# Find elements that appear in every sublist using set.
# Example
# data = [
#     [1, 2, 3, 4],
#     [2, 3, 5, 6],
#     [2, 3, 7]
# ]
# Expected Output
# {2, 3}

data = [
    [1, 2, 3, 4,4],
    [2, 3, 5, 6],
    [2, 3, 7],
    [2,1,1]
]

#to compare with all will target [0]

x = set(data[0]) #duplicate...

for i in data[1:]:
    #{1,2,3,4} = {1,2,3,4} & {2,3,5,6} = {2,3}
    #x = {2,3}
    #{2,3} = {2,3} & {2,3,7} = {2,3}
    x = x & set(i)

print(x)    


