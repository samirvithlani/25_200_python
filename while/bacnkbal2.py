chance = 3

while chance>0:
    print("remaining chances are ",chance)
    bal = int(input("enter bal min 10,0000* :"))
    if bal>=10000:
        print("account opened . bal = ",bal)
        break
    chance-=1