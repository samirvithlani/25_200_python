data1 = {"krishna","arjun","sahdev"}
data2 = {"ram","laxman","janki","sahdev"}

#union

#x =data1.union(data2)
x = data1 | data2
print(x)

#x = data1.difference(data2)
x = data1 -data2
print(x)

#x = data1.intersection(data2)
x = data1 & data2
print(x)

x = data1.symmetric_difference(data2)
print(x)

goa = {"amit","sumit","riya","priya","jay"}
mumbai = {"ajay","vijay","amit","parth","kunal"}
pune = {"kunal","neha","amit","raj","rajvi"}


#find person who have attended all city event
#find person who have attended mumbai and goa
#find person who have attended mumbai and pune
#find who have attended goa but not mumbai and pune

