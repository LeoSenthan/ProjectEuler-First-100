from math import sqrt
def prime_sieve(num):
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
#Chakravala Method
def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
 
    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k
 
        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
        x1 = x
    return x
 
L = 1000
print ("Project Euler 66 Solution:", max((pell(d),d) for d in prime_sieve(L)))