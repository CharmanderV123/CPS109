in_list = [1, 2, 3, 4, 5, 6, 7, 8]
expbool = False

half = int((len(in_list))/2)
result = []

#Out Shuffle
if expbool == True:
    for i in range(half):
        result.append(in_list[i])
        result.append(in_list[i+half])

#In Shuffle
elif expbool == False:
    for i in range(half):
        result.append(in_list[i+half])
        result.append(in_list[i])
else:
    result = "Something Went Wrong"

print(result)