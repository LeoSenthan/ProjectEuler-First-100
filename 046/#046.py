#Sieve of Eratosthenes
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
primes=SieveOfEratosthenes(1000000)

n=7
while True:
    n+=2
    flag=False
    if n not in primes:
        for square in range(1,int(sqrt(n))):
            if n-2*(square**2) in primes:
                flag=True
    else:
        flag=True
    if flag==False:
        print(n)
        exit()