#Venujan Suthakaran
#September 26, 2024
#CPS109 Lab 2

def squirrel_play(temp, is_summer):
  if (60<=temp<=90 and is_summer == False) or (is_summer == True and 60<=temp<=100):
    result = True
  else:
    result = False
  return result
