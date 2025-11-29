#Number of divisors = d(n) = (a+1)*(b+1)*(c+1) where a b and c are the powers of the prime factors of n

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

current,n=1,2
while True:
    current=current+n
    n=n+1
    factors=sorted(primeFactors(current))
    distinct=list(set(factors))
    total=1
    for prime in distinct:
        total=total*(factors.count(prime)+1)
    if total>=500:
        print(current)
        exit()
