subjects = ["java","python","c","cpp","node"]
print(subjects)

#add 1 more elm..
subjects.append("JavaScript") #end
print(subjects)

#newsub = ["maths","science"]
#subjects.extend(newsub)
subjects.extend(["maths","science"])

print(subjects)

#specific index

subjects.insert(3,"DataStructure") #3 index,"elment"
print(subjects)