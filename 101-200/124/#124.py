import math
def uniqueprimeFactors(n):
    factors=[]
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    factors=list(set(factors))
    return factors
unsortedlist=[]
for n in range(1,100001):
    factors=uniqueprimeFactors(n)
    result=1
    for factor in factors:
        result*=factor
    unsortedlist.append([n,result])
sortedlist=sorted(unsortedlist,key=lambda x:x[1])
print(sortedlist[9999])