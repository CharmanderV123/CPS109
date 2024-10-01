#Venujan Suthakaran
#September 26, 2024
#CPS109 Lab 2

#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
#sorta_sum(3, 4) → 7
#sorta_sum(9, 4) → 20
#sorta_sum(10, 11) → 21

#Answer One
#def sorta_sum(a, b):
#  result = 0 
#  for i in range (10,19):
#    if i == a+b:
#      result = 20
#  
#  if result != 20:
#    result = a+b
#  
#  return int(result)
#
#print("7 : ", sorta_sum(3,4))
#print("20 : ", sorta_sum(9,4))
#print("21 : ", sorta_sum(10,11))
#print("19: ", sorta_sum(9,10))
#print("10: ", sorta_sum(1,9))

#Error: Other Tests Failed

def sorta_sum(a, b):
  if 10<=(a+b)<=19:
    result = 20
  else:
    result = a+b
  return result