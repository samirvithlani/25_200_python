nums = [4,5,1,2,5,3,1]

#raj parth kunal amit raj kunal ajay
checked = set() #blank 

for i in nums:
    #4 in {} -false
    #5 in {4}
    #1 in {4,5}
    #2 in {4,5,1} 
    #5 in {4,5,1}
    if i in checked:
        print(i) #5
        break
    checked.add(i) #4,5,1,2