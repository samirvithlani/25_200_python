#we can return single value at a time..

users = ["bob","janmay","janam","madam","naman","ajay"]
#["palindrome","not p..","not..","pal.."]

#userswithlable = ["palindrome" for i in users]
#userswithlable = [i for i in users if i==i[::-1]]
userswithlable = ["palindrome" if i == i[::-1] else "not palidrome.." for i in users]
print(userswithlable)

numbers = [12,23,45,78,9,42,2234,564,3,567]
#numberlab = ["even","odd",...]
#numberslab = [i for i in numbers if i %2 ==0]
numberslab = ["even" if i %2 ==0 else "odd" for i in numbers]
print(numberslab)

names = ["amit shah","narendra modi","rajkumar","rohit sharma"]
#nameswithlab = [i for i in names]
#nameswithlab = [i for i in names if " " in i]
nameswithlab = ["space" if " "in i else "not space" for i in names]
print(nameswithlab)


data = ["Jay","kumar","VIRAT","Kohli","Sachin","tendulkar"]
#isUpper #isLower

#datalab = [i for i in data if i.isupper()]
datalab = ["upper" if i.isupper() else "not lower" for i in data]
print(datalab)



