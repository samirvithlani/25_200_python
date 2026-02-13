#marks.txt
file = open("marks.txt","r")
lines = file.readlines() #[] list

#result..
file2 = open("result.txt","w")
for line in lines:
    name,marks=line.strip().split(",")
    marks = int(marks)
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks>=50:
        grade="C"        
    else:
        grade="FAIL"    
    
    file2.write(f"{name} - {marks} - {grade}\n")        

file2.close()    