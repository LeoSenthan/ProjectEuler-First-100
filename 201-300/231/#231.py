#Binomial coeffficient (20 000 000 C 15 000 000)
# = 20 000 000 ! / (15 000 000 ! * 5 000 000 !)
# = 15 000 001 - 20 000 000 / 5000000!
#Legendre's formula 

import math

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
primes=SieveOfEratosthenes(20001000)

def Legendres(n):
    factors=[]
    current=0
    while True:
        if primes[current]>n:
            break
        power=1
        count=0
        while True:
            if math.floor(n/(primes[current]**power))==0:
                factors.append([primes[current],count])
                current+=1
                break
            else:
                count+=math.floor(n/primes[current]**power)
                power+=1
    return factors

factorial20=Legendres(20000000)
factorial15=Legendres(15000000)
factorial5=Legendres(5000000)

for factor in range(0,len(factorial5)):
    factorial15[factor][1]+=factorial5[factor][1]
for factor in range(0,len(factorial15)):
    factorial20[factor][1]-=factorial15[factor][1]
print(factorial20)
total=0
for factor in range(0,len(factorial20)):
    total+=factorial20[factor][0]*factorial20[factor][1]
print(total)