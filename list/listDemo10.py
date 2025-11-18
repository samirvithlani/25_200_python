data = [["Monday",100],["Tuesday",200],["Wednesday",250],["Thursday",400],["Friday",430],["Saturday",340],["Sunday",630]]

#increse Thursday unit by 20%
#decrese Saturday unit by 25%
#add 20 units in Monday

#print updated list after this

data[3][1] = data[3][1] + data[3][1] *0.2
print(data)


data = [[1,2,3],[4,5,6],[7,8,9]]
#print in matrix form  and do row wise sum and print in every row

#1 2 3 = 6
#4 5 6 = 15
sum=0
for i in range(0,len(data)):
    #[][][]
    for j in range(0,len(data[i])):
        sum = sum + data[i][j]
        print(data[i][j],end=" ")
    print("sum =",sum)    #6
    print()    
    sum=0