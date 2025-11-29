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

minratio,answer=100000000,5
for n in range(2,10000000):
    factors,totient=primeFactors(n),n
    for factor in factors:
        totient=totient*(1-1/factor)
    if (n/totient)<minratio and sorted(str(int(totient)))==sorted(str(n)):
        minratio,answer=n/totient,n
        print(answer)
print(answer)