import random

over = int(input("enter no of overs you want to play:"))
totalballs = over * 6
totalrun = 0
for i in range(1,totalballs):
    run = random.randint(1,6)
    print(f"ball {i} - run ={run}")
    totalrun+=run

print(totalrun)    
    