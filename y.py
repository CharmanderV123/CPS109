items =[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
item_count = []
item_temp = []
k = 2
result = []
setitems = list(set(items))
print(setitems)
for item in setitems:
    item_count.append(k)

for i in items:
    if item_count[setitems.index(i)]>0:
        item_count[setitems.index(i)]-=1
        result.append(i)

print(item_count)
print(result)