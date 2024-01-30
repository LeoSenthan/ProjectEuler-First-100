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
checks=SieveOfEratosthenes(1000000)
#b has to be positive prime
#max number of primes is b-1 since if it reached b it would be b**2 +ab + b and b would be a factor
maxcount,truea,trueb=0,0,0
for b in primes:
    for a in range(-b,1000):
        counter,n=-1,0
        while True:
            n=n+1
            checker=(n**2)+(a*n)+b
            if checker not in checks:
                break
            counter+=1
        if counter>maxcount:
            maxcount,truea,trueb=counter,a,b
print(truea*trueb)
#slow but works