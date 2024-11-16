def rlen(rlist):

    if rlist == []:
        return 0
    
    else:
        rlen(rlist[1:])
        return 1+rlen(rlist[1:])
    
print(rlen(['a', 2, 3]))