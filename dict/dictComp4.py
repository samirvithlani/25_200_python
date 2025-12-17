



d = {"a": 10, "b": "hello", "c": 3.5, "d": True, "e": 50}


d1 = {i:j for i,j in d.items() if type(j)==int or type(j)==float}
print(d1)
#{"a": 10, "c": 3.5, "e": 50}
