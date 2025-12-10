'''

#declare dict =
players = {"virat":135,"rohit":65,"hardik":70,"yashshvi":121}

get player name from user input and remove it if player name is present
hint: use in operator
'''

players = {"virat":135,"rohit":65,"hardik":70,"yashshvi":121}

name = input("enter playaer name to delete data :")
if name in players:
    players.pop(name)

print(players)    

sales = {"monday":100,"tuesday":200,"wednesday":300}
#10 % profit
#print

salesprofit ={}

for i,j in sales.items():
    salesprofit[i] = j+ j*0.1

print(salesprofit)    