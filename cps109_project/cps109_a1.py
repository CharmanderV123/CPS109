#Venujan Suthakaran
#Description
#This program is designed to take the accounting information such as income, costs, and networths of a person. 
#This is done through modifying a file called accounts.txt, this files contains numbers separated by commas and they include | dividing the income from the costs from the networth. 
#Im unsure if I can complete the networth writing aspect though. 
#This program uses the information in the file to display the total income, costs, and networth of the user.
#By using arithemetic operations this program calculates networth, total costs, and total profits
#Utilizing functions for calculating the values of income, cost, and networth the program becomes more efficient
#I could turn majority of this into a class

#NOTE: You May Need to Modify accounts.txt path modify variable value below
#This variable makes it easy for the user to modify the path of the accounts.txt file (CSV support soon to come)
path = "C:/Users/charm/OneDrive/Documents/GitHub/CPS109/cps109_project/accounts.txt"


#This function opens the accounts.txt file to find the income numbers entered in the file
#Utilizing the split function to split at the separators specified such as "|" to create separate lists for income, cost, and networth allows the program to look at each attribute independantly
#Splitting again at "," allow the values corresponding to the respective attribute to be obtained
#At the end the function sums up the corresponding values and returns the total income
def incomecalc():
    accountslist = []
    sum = 0
    result = "Something Went Wrong"
    accounts = open(path,"r")
    for line in accounts:
        accountslist = line.split("|")
    for item in accountslist[0].split(","):
        sum+=int(item)
    accounts.close()
    result =sum
    return result

#This is the function that takes care of the modifications to the income and costs of the user
def mod(atr,mod):
    result = ""
    accountslist = []

#Opens file here is read mode to save data in a variable accountslist
    accounts = open(path,"r")

    for line in accounts:
        accountslist = line.split("|")
    accounts.close()
    
#During the next few steps the function writes to the files the new modfied data replacing and overwriting existing data

#The function goes to index 0 of accountslist as that is where the values for income are saved, and proceeds to modify them if atr = "Income"
    if atr == "Income":
        accountslist[0] = mod
        accounts = open(path,"w")
        for item in accountslist:
            result= result + item+ "|"
        accounts.write(result)

#The function goes to index 1 of accountslist as that is where the values for cost are saved, and proceeds to modify them if atr = "Cost"
    elif atr == "Cost":
        accountslist[1] = mod
        accounts = open(path,"w")
        for item in accountslist:
            result= result + item+ "|"
        accounts.write(result)
    accounts.close()

#This function opens the accounts.txt file to find the cost numbers entered in the file
#Utilizing the split function to split at the separators specified such as "|" to create separate lists for income, cost, and networth allows the program to look at each attribute independantly
#Splitting again at "," allow the values corresponding to the respective attribute to be obtained
#At the end the function sums up the corresponding values and returns the total cost
def costcalc():
    accountslist = []
    sum = 0
    result = "Something Went Wrong"
    accounts = open(path,"r")
    for line in accounts:
        accountslist = line.split("|")
    for item in accountslist[1].split(","):
        sum+=int(item)
    accounts.close()
    result = sum
    return result

#This function calls the above two functions to determine the difference providing the networth
def networth():
    return incomecalc()-costcalc()

#choice1 is initialized to -1 so the while loop stays unaffected. 0 was not used as it seemed more reasonable to use as the exit indicator
choice1= -1

#The main program starts here it is designed inside a while loop to allow the user to run this file once to access all functionalities
while(choice1 != 0):

#An intro statement or mini GUI for the user, not as effective as modern day UIs but good enough for a terminal based one

    print("||Welcome to my Project||\n")
    print("Enter the respective number to enter that respective program")
    print("1. Income")
    print("2. Cost")
    print("3. Networth")
    print("Enter 0 to Quit Program ")

#User selects which functionality they would like to access with the option to quit the program
    choice1 = int(input("Enter your Selection: "))

#User is given the opportunity to select whether they want to modify or calculate your income (Depending on how far I get it may just be Calculate Income)
    if choice1 == 1:
        print("\nWhat would you like to do?")
        print("1. Modify Income")
        print("2. Calculate Income")
        choice2 = int(input("Enter your selection: "))
    
#This part of the program when it receives choice2 value as 1 it will acquire the new modified values of income from the user
#Then the program replaces the values in the file using the defined mod function and prints out the new income. 
        if choice2 ==1:
            imod = input("Enter a list of income values separated by commas: ")
            mod("Income",imod)
            print("Your New Income is: ", incomecalc())

#This part of the program reads the income values in the accounts.txt file print the monthly and annual incomes of the user
        elif choice2 == 2:
            print("\nThis is your monthly income: ",incomecalc())
            print("This is your annual income: ", 12*incomecalc(),"\n")

#In the case the user enters a number outside what was given the program restarts
        else:
            print("\nIncorrect Value Given Program will now Restart")

#User is given the opportunity to select whether they want to modify or calculate your Costs (Depending on how far I get it may just be Calculate Costs)
    elif choice1 == 2:
        print("\nWhat would you like to do?")
        print("1. Modify Cost")
        print("2. Calculate Cost")
        choice2 = int(input("Enter your selection: "))

#This part of the program when it receives choice2 value as 1 it will acquire the new modified values of cost from the user
#Then the program replaces the values in the file using the defined mod function and prints out the new cost.         
        if(choice2==1):
            imod = input("Enter a list of cost values separated by commas: ")
            mod("Cost",imod)
            print("Your New Cost is: ", costcalc())

#This part of the program reads the income values in the accounts.txt file print the monthly and annual costs of the user
        elif choice2 == 2:
            print("\nThis is your monthly costs: ",costcalc())
            print("This is your annual costs: ", 12*costcalc(),"\n")

#In the case the user enters a number outside what was given the program restarts
        else:
            print("\nIncorrect Value Given Program will Now Restart")

#This portion of the program determine the users networth on a monthly and annual basis, while also providing feedback on the financial situation of the user
    elif choice1 == 3:
        print("\nCalculating Networth ...")
        print("This is your current Networth this month: ", networth())
        print("This is your projected Networth after a year: ", 12*networth())

#Provides user with feedback on financial position
        if networth()>0:
            print("Positive Networth, Great Work\n")
        elif networth()<0:
            print("Negative Networth, Increase Income or Decrease Costs\n")
        else:
            print("Networth is 0\n")

    elif choice1==0:
        print("Program is Now Ending ...")

#In the case the user enters a number outside what was given the program restarts
    else:
        print("\nIncorrect Value Given Program will Now Restart")