# season = input("please enter season name :")

# match season:
#     case "summer":
#         print("please dont go out if you are in ahmedbad")
#     case "monsoon":    
#         print("please keep umbrella with you else '_' ")
#     case "winter":
#         print("winter is coming !!")    
#     case _:
#         print("find your own peace!!!")        


season = input("please enter season name :")

match season:
    case "summer" | "SUMMER" | "S" :
        print("please dont go out if you are in ahmedbad")
    case "monsoon" | "MONSOON" | "M":    
        print("please keep umbrella with you else '_' ")
    case "winter" | "WINTER" | "W":
        print("winter is coming !!")    
    case _:
        print("find your own peace!!!")        
                