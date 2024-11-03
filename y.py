tiles = [(6, 5), (5, 2), (2, 3), (3, 6)]
result = False
count = 0
for items in range(len(tiles)-1):
    if tiles[items][1] == tiles[items+1][0]:
        print("tiles",tiles[items][1])
        print("tiles2",tiles[items+1][0])
        count+=1
        print(count)
if (tiles[0][0] == tiles[len(tiles)-1][len(tiles[0])-1]) and (count == len(tiles)-1):
    result = True
print(tiles[0][0])
print(tiles[len(tiles)-1][len(tiles[0])-1])
print(result)