# def chcekdata(data):
#     passstu = []
#     for i,j in data.items():
#         if j>70:
#             passstu.append(i)
#     return passstu        


def chcekdata(data):
    return [i for i,j in data.items() if j>70]


users  ={"raj":100,"parth":90,"jay":77,"ajay":65,"neha":60,"kunal":65}
x = chcekdata(users)
print(x)
#["raj","parth","jay"]
#return names whoese marks> 70