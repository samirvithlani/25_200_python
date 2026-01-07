# def calc(*args):
#     sum=0
#     for i in args:
#         sum = sum +i
#     return sum    


# ans = calc(10,20,30,40,50,60)
# print(ans)

def calc(op,*args):
    ans =0
    if op =="sum":
        for i in args:
            ans = ans +i
        return ans
    elif op == "mul" :
        ans =1
        for i in args:
            ans = ans *i
        return ans
    return ans    
        


#ans = calc("sum",10,20,30,40,50,60)
ans = calc("mul",1,2,3,4,5)
print(ans)