from utils import add,sub #indiv..
#file
import validation  #file
import listfun as l #alias

x = add(10,20)
print(x)
s = sub(100,20)
print(s)

ans = validation.checkString("")
print("ans..",ans)

x = l.upperList(["amit","sumit","raj","parth"])
print(x)