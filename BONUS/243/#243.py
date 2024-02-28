#relative prime
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
  return factors,set(factors)
ratio,denominator=1,11
while ratio>4/10:
    denominator+=1
    count=denominator
    factors,uniquefactors=list(primeFactors(denominator))
    for unique in list(set(factors)):
        count/=unique
        count*=(factors.count(unique)-1)
    print(count,denominator)
    ratio=count/denominator
print(denominator)