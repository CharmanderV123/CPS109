#Venujan Suthakaran
#September 26, 2024
#CPS109 Lab 2

# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. 
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
#caught_speeding(60, False) → 0
#caught_speeding(65, False) → 1
#caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed = speed - 5
  if speed<=60:
    result = 0
  elif 61<=speed<=80:
    result = 1
  elif speed>=81:
    result = 2
  return result

print("0 : ", caught_speeding(60, False))
print("1 : ", caught_speeding(65, False))
print("0 : ", caught_speeding(65, True))