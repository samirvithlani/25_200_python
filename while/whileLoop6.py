#take balance from user to open an account
#min balance should be 10,000
#if user has inserted less then 10k ask again enter balance 
#ask user untill he/sbhe is not inserting greter then or equal 1000
#if correct print balance
bal =0
while True:
    bal = int(input("enter balance :"))
    if bal>=10000:
        break

print("balance = ",bal)    