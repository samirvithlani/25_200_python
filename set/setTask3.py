data = "swiss"

watched = set() #blank set
count ={} #dict

for c in data:
    #swiss
    if c in count:
        #{s:2,w:1,i:1}
        ##{s:3,w:1,i:1}
        count[c]+=1
    else:
        #{s:1,w:1,i:1}
        count[c]=1
        watched.add(c) #{s,w,i}


for x in data:
    #x = s
    #x = w =1
    if count[x]==1:
        print(x)
        break