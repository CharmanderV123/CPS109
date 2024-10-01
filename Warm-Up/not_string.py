def not_string(str):
  if str[:3] == "not":
    result = str
  else:
    result = "not "+str
  return result

#Given Answer
#def not_string(str):
  #if len(str) >= 3 and str[:3] == "not":
  #  return str
  #return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3