# Sequence after subtracting one= 1/2,2/5,5/12,12/29,29,70,70/169,169/408,408/1393
#To work out next denominator formula is previous numerator * 2 + the numerator before the last
#To work out numerator is the previous denominator
numerator,denominator,count=[1,2,5],[2,5,12],0
while len(denominator)<1000:
    numerator.append(denominator[-1])
    denominator.append(numerator[-1]*2+numerator[-2])
for top in range(0,len(numerator)):
    if len(str(numerator[top]+denominator[top]))>len(str(denominator[top])):
        count+=1
print(count)