#e denominators are 3,4,7,32,39,71,465,536
#pattern is sum of previous two but then it is current*2n +previous
#for example 32 = 7*4+4 and 465 = 71*6+39
#numerator pattern is sum of previous two then jump of previous*4 +previous of previous

n,numerators,jump,total=5,[8,11,19],2,0
while n<100:
    n+=1
    if n%3==0:
        jump+=2
        numerators.append(numerators[-1]*jump+numerators[-2])
    else:
        numerators.append(numerators[-1]+numerators[-2])
for digit in str(numerators[-1]):
    total+=int(digit)
print(total)