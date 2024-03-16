#R(k)= (10*k-1)/9 remainder of 10*k and 9*n is 1 if r(k) can be divided by n
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
primes=SieveOfEratosthenes(1000001)
sum,n=0,0
for p in primes:
    if pow(10, 10**9, 9*p)==1:
        n += 1
        sum += p
        if n==40: break
print (sum)