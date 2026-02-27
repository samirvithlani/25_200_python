
from files_task import store
from calc import cal_marks,cal_pers

marks = [80,90,78,67,71]

total = cal_marks(marks)
print("total",total)
pers = cal_pers(total,len(marks))
print("pers",pers)

store("result1.txt","amit",total,pers)