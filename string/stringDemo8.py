#a,e,i,o,u
#royal -->2

name = "royal"
count =0

# for i in range(0,len(name)):
#     if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
#         count+=1


for i in name:
    if i in "aeiouAEIOU":
        count+=1

print(f"no of vo.... in {name} = {count} ")        