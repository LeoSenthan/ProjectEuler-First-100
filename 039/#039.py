#pythagorean formula
count,pvalue=0,0
from math import sqrt
for p in range(1,999):
    current=0
    for a in range(1,p//4):
        for b in range(a+1,(p-a)//2):
            c=sqrt(a**2+b**2)
            if a+b+c==p:
                current+=1
    if current>count:
        count,pvalue=current,p
print(pvalue)