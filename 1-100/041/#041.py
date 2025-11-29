#9 and 8 digits can not be done as they sum to 45 and 36 which are both divisble by 3
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
primes=SieveOfEratosthenes(10000000)

max,checker=0,"1234567"
for prime in primes:
    Flag=True
    for char in range(0,len(str(prime))):
        if checker[char] in str(prime):
            pass
        else:
            Flag=False
            break
    if prime>max and Flag==True:
        max=prime
print(max)
