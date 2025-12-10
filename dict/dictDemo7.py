#remove operation...

players = {"virat":135,"rohit":65,"hardik":70,"yashshvi":121}
print(players)

#pop(key)
# players.pop("hardik")
# print(players)

removedElm = players.pop("hardik")
print(removedElm)
print(players)

# players.popitem()
# print(players)

removedData = players.popitem()
print("remvoing...",removedData)
print(players)