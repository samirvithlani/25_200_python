import random as r #alias
print(r.random())

names =["ajay","raj","parth","neha","sumita","kunal"]

randomName = r.choices(names,k=2)
print(randomName)

print(r.sample(names,k=3))