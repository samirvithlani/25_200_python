sales = {"Mon":100,"Tue":120,"Wed":150}
#20% increse..
saleswithprofit ={}

#i=key
#j = value

# for i,j in sales.items():
#     profit = j + j*0.2
#     saleswithprofit[i] = profit

saleswithprofit ={i:(j+j*0.2) for i,j in sales.items()}
print(saleswithprofit)    
    