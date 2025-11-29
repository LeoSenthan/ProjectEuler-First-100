#primes are in range of 1000 to 9999
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

primes=SieveOfEratosthenes(10000)
removeprimes=SieveOfEratosthenes(1000)
primes=primes[len(removeprimes)+1:]
for prime in primes:
    if prime+3330 in primes and sorted(str(prime))==sorted(str(prime+3330)):
        if prime+6660 in primes and sorted(str(prime))==sorted(str(prime+6660)):
            print(prime,prime+3330,prime+6660)
            