from math import sqrt
def SieveOfEratosthenes(num):
  list1=[]
  prime = [True for i in range(num+1)]
  p = 2
  while (p * p <= num):
      if (prime[p] == True):
          for i in range(p * p, num+1, p):
              prime[i] = False
      p += 1
  for p in range(2, num+1):
      if prime[p]:
          list1.append(p)
  return list1
primes=SieveOfEratosthenes(1000)
#chakravala method
result,answer=0,0
for prime in primes:
    p, z, x1, y, sd = 1,1,1,0,sqrt(prime)
    while z != 1 or y == 0:
        p = k * (p/z+1) - p
        p = p - int((p - sd)/k) * k
        x = (p*x1 + prime*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - prime) / k
        x1 = x
    if x>result:
        answer,result=prime,x
print(answer)