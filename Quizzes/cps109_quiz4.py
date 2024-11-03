num = int(input("Enter a Number: "))

if num>100:
    print("Too much work, no thanks")

elif num <1:
    print("N must be greater than 1")

else:
    for i in range(1,num+1,1):
        result =""
        if i%3==0:
            result = result+"Fizz"
        if i%5 == 0:
            result = result+"Buzz"
        if result == '':
            print(i)
        else:
            print(result)
    