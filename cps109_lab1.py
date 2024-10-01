#Venujan Suthakaran
#CPS109
#Lab 1
#September 10, 2024

# Question 1

celcius = float(input("Enter the Temperature in Celcius: "))
fahrenheit = celcius*(9/5)+32
kelvin = celcius + 273.15

print(celcius, " degrees celcius in degrees fahrenheit is: ", fahrenheit)
print(celcius, " degrees celcius in kelvins is: ", kelvin)

# Question 2
print("\n Question 2 Quadratic Formula")
a_value = float(input("Enter the a-value: "))
b_value = float(input("Enter the b-value: "))
c_value = float(input("Enter the c-value: "))

x_value_1 = ((-1)*(b_value)+(b_value**2 - (4)*(a_value)*(c_value))**0.5)/(2*a_value)
x_value_2 = ((-1)*(b_value)-(b_value**2 - (4)*(a_value)*(c_value))**0.5)/(2*a_value)

print("The Possible Roots are {:g} and {:g}".format(x_value_1, x_value_2))

#Question 3
print("\n Question 3")
num1 = float(input("Enter a num: "))
num2 = float(input("Enter a num: "))
num3 = float(input("Enter a num: "))
h_value = max(num1, num2, num3)

print((num1+num2+num3-h_value)>h_value)

#Question 4
print("\n Question 4")
aa_value = float(input("Enter the a value: "))
area = (1/4)*((5*(5+(2*(5**0.5))))**0.5)*(aa_value**2)

#Question 5
print("\n Question 5")
n_value = int(input("Enter the term number: "))
phi = ((5**0.5)+1)/2
f_value = ((2+phi)/5)*(phi**n_value)+((3-phi)/5)*(phi**((-1)*(n_value)))
print("The Function Value is: ", round(f_value,2))