#Find first 25 prime pairs
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
primes=SieveOfEratosthenes(100000000)
total,check=0,[]
for prime in primes:
    if str(prime**2)!=str(prime**2)[::-1] and str(prime**2)[-1]!="0":
        if sqrt(int(str(prime**2)[::-1]))%1==0 and int(sqrt(int(str(prime**2)[::-1])))  in primes:
                total+=prime**2
                print(prime**2)
                check.append(prime**2)
                if len(check)==50:
                    break
print(sum(check))
print(len(check))