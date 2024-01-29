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
#number will be greater than 500000 since number of primes decreases as number increases
max,number=0,0
for i in range(500000,1000001):
    factors=list(set(primeFactors(i)))
    count=i
    for factor in factors:
        count=count*(1-(1/factor))
    if i/count>max:
        max,number=i/count,i   
        print(number)
#since 510510 has not changed for a while it is probably correct