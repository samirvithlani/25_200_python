names = ["naman","raj","bob","madam","jay","racecar"]
palindromeNames = []

for i in names:
    #namen == naman
    #raj == jar
    if i == i[::-1]:
        palindromeNames.append(i)

print(palindromeNames)        
        