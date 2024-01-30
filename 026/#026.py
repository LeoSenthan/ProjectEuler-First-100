#check primes since multiples will result in duplicate lengths
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
nvals=SieveOfEratosthenes(1000)

maxcount,answer=0,0
for n in nvals:
    rest,len=1,0
    while rest!=0:
        if (rest*10)%n==1:
            break
        rest,len=(rest*10)%n,len+1
        if len>maxcount:
            maxcount,answer=len,n
print(answer)
