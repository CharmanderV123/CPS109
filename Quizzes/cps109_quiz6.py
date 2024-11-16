num  = int(input("Num is: "))
count = 0
for i in range(2, num):
    if num%i ==0:
        count+=1
if count>0:
    print("Not Prime")
else:
    print("Prime")