#Venujan Suthakaran
#CPS109
#Quiz 1
#September 17, 2024
import math
num_of_side = int(input("Enter the number of sides: "))
side_length = float(input("Enter Side Length: "))

perimeter = num_of_side*side_length

#print(perimeter)

apothem = (side_length)/(2*math.tan(math.pi/num_of_side))

#print(apothem)

area = 0.5*apothem*perimeter

print("This is the area:", round(area, 2))
