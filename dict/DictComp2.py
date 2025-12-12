users = ["amit","sumit","ajay","raj"]
#{"amit":"AMIT","sumit":"SUMIT"}
userswithupper = {}
for i in users:
    userswithupper[i] = i.upper()

print(userswithupper)    

#userswithupper1 = {i:i for i in users}
userswithupper1 = {i:i.upper() for i in users}
print(userswithupper1)
#{"a":amit","s":"sumit"/...}

userswithinital = {i[0]:i for i in users}
print(userswithinital)