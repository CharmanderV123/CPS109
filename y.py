items=[1,2,3,3.4,5.4,3.6,"serdsfs","sdfsdf"]

result = [0, 0.0, ""]
for item in items:
    if type(item) == float:
        if result[1] < item:
            result[1]=item
    elif type(item) == int:
        if result[0] < item:
            result[0]=item
    elif type(item) == str:
        if len(result[2])<len(item):
            result[2]=item
print(result)
