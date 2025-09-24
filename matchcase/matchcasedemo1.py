no1 = int(input("enter no 1:"))
no2 = int(input("enter no 2:"))


choice = int(input("Enter 1 for  add \n Enter 2 for sub \n Enter 3 for mul \n Enter 4 for Div"))

# if(choice ==1):
# elif(choice==2)

#switch(choice){
#    case 1:
#}

match choice:
    case 1:
        print("add operation ::")
        c = no1 + no2
        print(f"ans = {c}")
    case 2:
        print("sub operation ::")
        c = no1 - no2
        print(f"ans = {c}")
    case 3:
        print("mul operation ::")
        c = no1 * no2
        print(f"ans = {c}")        
    case 4:
        print("add operation ::")
        c = no1 // no2
        print(f"ans = {c}")   
    case _:
        print("invalid choice ::")     
            
            
        
