#Algorithm to calculate prime factors
import math
def primeFactors(n):
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
  return factors

ratio,n,layer,primecount,totaldiag=1,1,0,0,1
while ratio>0.1:
    layer+=2
    for i in range(4):
        n+=layer
        if len(primeFactors(n))==1:
            primecount+=1
    totaldiag+=4
    ratio=primecount/totaldiag
print(layer+2)
    