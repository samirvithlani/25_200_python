# = : equal
# it assign right side value to left side varible
# a = 100

a = 100
b = 200
temp=0
#swap value
#with using temp variable
#witout using temp variable.

temp = a #temp =100
a = b    #a =200
b = temp #b =100

print("value of a = ",a)
print("value of b = ",b)

#without using 3rd variable..
x = 10
y = 20

x = x + y #x = 30
y = x - y # y =30 -20 = 10
x = x - y # x = 30 - 10 = 20

print("value of x = ",x)
print("value of y = ",y)


x = 5
y = 10

x = x * y #x =  50
y = x/y   #y = 50 / 10 = 5
x = x/y  #x = 50 /5 = 10

print("value of x = ",x)
print("value of y = ",y)



# no1 =100
# no2 =200

# no1,no2 =100,200
# print("value of no1 = ",no1)
# print("value of no2 = ",no2)

no1 = 100
no2 = 200

no1,no2 = no2,no1
print("value of no1 = ",no1)
print("value of no2 = ",no2)