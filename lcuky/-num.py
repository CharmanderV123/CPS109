num = int(input("Enter the num: "))
count0 = 0
count7 = 0
result = 0
for i in range(num):
    str_num = str(i)
    for x in str_num:
        if x == "0":
            count0+=1
        elif x == "7":
            count7 +=1
    if count7>count0:
        result+=i

print(result)