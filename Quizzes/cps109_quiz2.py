num = int(input("Enter the integer: "))
factor_list = []
for i in range(2,10):
    if num%i==0:
        factor_list.append(i)

if len(factor_list)>=1:
    print("The Factors of the num between 2 and 10 are: ", ', '.join(map(str, factor_list)))
else:
    print("This number has no factors between 2 and 10")