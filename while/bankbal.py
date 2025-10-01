bal =0
chance=5
for i in range(1,chance):
    print("remainng chances are ",chance-i)
    bal = int(input("enter balance :"))
    
    #10000
    if bal>=10000:
        print("balance = ",bal)
        break


