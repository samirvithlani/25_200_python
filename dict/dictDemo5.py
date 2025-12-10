#{key:value}

#empty
# data = {}
# print(data)
# print(type(data))


data = {101:"Ahmedabad",102:"surat",103:"gandhinagr"}
print(data)
#variable[keyname]
#if key is not presetnt it will throw exception...
print(data[101])

#dict value add...
#variable[new key] = new value
data[105] = "Rajkot"
print(data)
#if key is already present
data[102] = "Gandhinagar"
print(data)

#if new dict need to add..
data.update({106:"Amreli",107:"botad"})
print(data)