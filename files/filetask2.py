file = open("fruits.txt","r")
line = file.readlines()

for i in line:
    print(i.strip().split(","))    

fruitName = input("enter fruit name to buy")
qty = int(input("enter qty to buy"))

file2 = open("bill.txt","w")
for i in line:
    name,price,disount = i.strip().split(",")
    price = int(price)
    if name == fruitName:
        total = price * qty
        file2.write(f"{name} - {qty} - {total}")
    
        
