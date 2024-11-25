
sum = 0
accountslist = []
accountslistitem = []
accounts = open("C:/Users/charm/OneDrive/Documents/GitHub/CPS109/cps109_project/accounts.txt","r")
for line in accounts:

    accountslist=line.split("|")
    print(line)
    print (accountslist)
for item in accountslist[0].split(","):
    sum+=int(item)

accounts.close()
print(sum)