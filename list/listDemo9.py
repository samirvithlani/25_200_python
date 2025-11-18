# enter player name 
# enter score

plyaer_score =[]

#i =0
#i =1
for i in range(0,3):
    name = input("Enter Player Name :") #Virat ,Rohit
    score = int(input("Enter Player Score")) #102 , 264
    #[["Virat",102],["Rohit",264]]
    plyaer_score.append([name,score])

print(plyaer_score)    
    
#insted of range loop    

for i in plyaer_score:
    for j in i:
        print(j,end=" ")
    print()        