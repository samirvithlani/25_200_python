#any all

data = ["parth","",None,"abc"]
print(any(data))
print(all(data))


numbers = [4,5,5,4]#zero fals  non zero true
print("any",any(numbers))
print(all(numbers))

#conditions

marks = [23,24,21,22,25]
#all subject 20>
flag = all(m>24 for m in marks)
print("all marks",flag)

flag = any(m>=26 for m in marks)
print("flag any ",flag)

roles = ["viewer","editor"]

is_admin = any(r=="admin" for r in roles)
print(is_admin)
