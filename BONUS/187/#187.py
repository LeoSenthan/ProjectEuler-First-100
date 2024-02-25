# Formula is number of semprimes is equal to integral between 1 and of number of primes below root n
# [number of primes(n/the kth prime)-k+1]
from math import sqrt
def primeCounter(num):
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
n=100000000
primes=primeCounter(int(10000))
count=0
for prime in primes:
    