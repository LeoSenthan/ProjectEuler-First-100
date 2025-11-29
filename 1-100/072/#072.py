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
  return list(set(factors))
#totient function with unique prime factors
total=0
for d in range(2,1000001):
    totient,factors=d,primeFactors(d)
    for factor in factors:
        totient=int(totient*(1-1/factor))
    total+=totient
print(total)