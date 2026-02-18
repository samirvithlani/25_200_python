firstName = ["raj","parth","amit","sumit","ajay"]
lastName = ["patel","shah","thakkar","jadav","sharma"]

file = open("fullname.txt","w")

for i in range(len(firstName)):
    file.write(f"{firstName[i]}-{lastName[i]}\n")

    
