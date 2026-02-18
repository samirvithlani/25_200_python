data= 12
print(type(data))
if type(data)==str:
    print("string...")

if isinstance(data,str):
    print("string...")    
else:
    print("not string")    