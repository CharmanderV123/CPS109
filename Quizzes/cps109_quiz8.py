def next_item(iteratorv):
        return(next(iteratorv, None))

items = iter([1, 2, 3, 4])
print(next_item((items)))
print(next_item((items)))
print(next_item((items)))
print(next_item(items))