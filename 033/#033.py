numerators=[]
denominators=[]
for numerator in range(10,100):
    strn=str(numerator)
    if numerator%10==0:
        pass
    else:
        for denominator in range(numerator+1,100):
            if denominator%10==0:
                pass
            else:
                strd=str(denominator)
                for char in strd:
                    if char in strn:
                        combo=int(strn.replace(char,"",1))/int(strd.replace(char,"",1))
                        if combo==numerator/denominator:
                            numerators.append(numerator)
                            denominators.append(denominator)
finaln,finald=1,1
for numerator in numerators:
    finaln=finaln*numerator
for denominator in denominators:
    finald=finald*denominator 
print(int(finald/finaln))