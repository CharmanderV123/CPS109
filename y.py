count = 0
items = [2, 1, 3]

if len(items) == 3:
    sorted_list = sorted(items)
    for i in range(3):
        if sorted_list[i] != items[i]:
            count+=1
    if count-1 == -1:
        result= 0
    else:
        result = count-1
else:
    result = -1
print(result)