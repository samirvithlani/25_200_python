data = {"GJ":"Gandhinagar","MH":"Mumbai","UP":"Lucknow","BH":"Patna","GJ":"Ahm"}
print(data)

#how to add new key value...
#1st way
data["PB"]="Chandigadh"
print(data)
#2nd way

data.update({"Goa":"Panji","Raj":"Jaipur","MH":"Pune"})
print(data)