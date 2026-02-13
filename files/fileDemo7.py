#with

# file = open("abc.txt","a")
# file.write("hello")
# file.close()
# file.write("ok")

with open("abcd.txt","w") as file:
    file.write("ok")
    #auto close
file.write("java")    