from collections import Counter

sports = [
"cricket","football","cricket","badminton",
"football","cricket","tennis","cricket",
"badminton","football","football"
]
#count frequecny
sports_count = Counter(sports)
print(sports_count)

#most popular
most_popular = sports_count.most_common(1)
print(most_popular)

# #sports only selected by 1 player
# oneplayer = sum(1 for s in sports_count if sports_count[s]==1)
# print(oneplayer)

oneplayer = [s for s in sports_count if sports_count[s]==1]
print(oneplayer)

match_type = [
"5v5","7v7","5v5","11v11",
"5v5","7v7","5v5","11v11",
"7v7","5v5"
]

#most demaanded match
#11v11 demanded ? >2 
match_count = Counter(match_type)
print(match_count.most_common(1))

if match_count['11v11']>=2:
    print("demanded")
