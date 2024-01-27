list=[]
import math
for n in range(2,28123):
    total=0
    for divisor in range(1,int(math.sqrt(n))):
        if n%divisor==0:
            total=total+divisor+n/divisor
    if total>divisor:
        list.append(n)
print(list)
