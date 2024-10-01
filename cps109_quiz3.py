#import re

password = input("Enter your password: ")
rpassword = input("Re-Enter your password: ")

#Variables for verification of each requirement 
pass1 = False
pass2 = False
pass3 = False
pass4 = False

#Code which Computes to see if Password meets Requirements

if password == rpassword:
    if len(password)>=8:
        pass1=True
    
    for i in password:
        if i.islower()==True:
            pass2 = True

        if i.isupper()==True:
            pass3 = True

        if i.isdigit()==True:
            pass4 = True

# Easy Method using Regular Expression Library
#    if bool(re.search(r'\d', password))==True:
#        pass4 = True

    if (pass1 and pass2 and pass3 and pass4) == True:
        print("Password Changed Successfully")
    else:
        print("Password not Complex Enough")
else:
    print("Passwords Must Match")

#Debugging Code
#print("Pass 1 ",pass1)
#print("Pass 2 ",pass2)
#print("Pass 2 ",pass3)
#print("Pass 4 ",pass4)