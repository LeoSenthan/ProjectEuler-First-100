from math import factorial
distinct=[]
#n!/(n-k)!
import math
def primeFactors(n):
  factors=[1]
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

n=0
while n<51:
    n+=1
    for k in range(0,n+1):
        current=(factorial(n)/(factorial(k)*factorial(n-k)))
        factors=primeFactors(int(current))
        if len(factors)==len(list(set(factors))):
            if current not in distinct:
                distinct.append(current)
print(len(distinct),len(list(set(distinct))))
print(sum(distinct)-51)