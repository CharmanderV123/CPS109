#Venujan Suthakaran
#September 26, 2024
#CPS109 Lab 2

def date_fashion(you, date):
    if (you>=8 or date>=8) and (you>2 and date>2):
        result = 2
    elif (you<=2 or date<=2):
        result = 0
    else:
        result = 1
    return result

print("2 : ", date_fashion(5,10))
print("0 : ", date_fashion(5,2))
print("1 : ", date_fashion(5,5))