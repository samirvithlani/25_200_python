reviews = {"raj":True,"amit":False,"parth":False,"jay":False,"kunal":True}
#if else...
reviewswithl = {}
for i,j in reviews.items():
    label = "fake"
    if j == True:
        label = "Not Fake"    
    
    reviewswithl[i] = label

print(reviewswithl)        

#compr

reviewswithl1 ={i:"fake" if j == False else "Not fake" for i ,j in reviews.items()}
print(reviewswithl1)


names  =["bob","jay","madam","neha","racecar"]
#{"bob":"pal","jay":"not pal.."}

#nameswithl = {i:"palindrome" for i in names}
nameswithl = {i:"palindrome" if i == i[::-1] else "not palindrome.." for i in names}
print(nameswithl)