def pos_neg(a, b, negative):
  if (negative == False and a<0 and b>0) or (negative == False and a>0 and b<0) or (negative == True and a<0 and b<0):
    result = True
  else:
    result = False
  return result

#Given Solution
#def pos_neg(a, b, negative):
#  if negative:
#    return (a < 0 and b < 0)
#  else:
#    return ((a < 0 and b > 0) or (a > 0 and b < 0))