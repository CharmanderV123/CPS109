#Venujan Suthakaran
#September 26, 2024
#CPS109 Lab 2

def cigar_party(cigars, is_weekend):
    if(40<=cigars<=60 and is_weekend==False) or (is_weekend==True and cigars>=40):
        result = True
    else:
        result = False
    return result

print("False : ",cigar_party(20, True))
print("True : ",cigar_party(50, True))
print("False : ",cigar_party(10, False))
print("True : ",cigar_party(90, True))
print("False : ",cigar_party(80, False))
print("False : ",cigar_party(20, True))