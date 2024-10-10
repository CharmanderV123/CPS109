num = int(input("Enter a num: "))
result = 0
str_num = str(abs(num))

#print(len(str_num))

for i in range(len(str_num)):
#    print(((temp//(len(str_num)-i))))
#    print((temp//(len(str_num))-i)%2)
    if ((num//(len(str_num))-i)%2 != 0):
#        print(temp)
#        print((len(str_num))-i)
#        print(((temp//(len(str_num))-i)))
        print(str_num[len(str_num)-(i+1)])
        result+=int(str_num[len(str_num)-(i+1)])

#    temp = temp-()
print (result)