#reverse string
#kunal
#lanuk

name = "raj"
#royal
#01234 --len 5
revname = ""
for i in range(len(name)-1,-1,-1):
    revname = revname + name[i]

print(revname)    

if name ==revname:
    print("name is palndrome ")
else:
    print("name is not palindrome...")    