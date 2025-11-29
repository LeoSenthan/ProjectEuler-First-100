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

primes=SieveOfEratosthenes(5000000)
answer = 0
for i in range(1, len(primes)):
    p = primes[i]
    for j in range(i):
        q = primes[j]
        l = 10000000//q
        if l < p: break
        r = p
        z = []
        while r <= l:
            s = r*q
            while s <= 10000000: s *= q
            z += [s//q]
            r *= p
        answer += max(z)
print (answer)