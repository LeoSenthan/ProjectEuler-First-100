#120 = 5! = 16
#Number of divisors is equal to (power+1)*(power+1)...
#So to optimize smallest number when prim2>prime1 the exponent of prime1>prime2
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
#divisors of 2**1 = 2**1
# 2**2 = 2**1 * 3**1 
# 2**3 = 2**3 *3**1
# 2**4 = 2**3 * 3**1 * 5**1
#Either increase smallest exponent number by that exponent + 1 or add a new prime number

count=4
factors=[[2,3],[3,1],[5,1]]
nextprime=3
while count<9:
    factors=sorted(factors,key=lambda a:a[1])
    comparison=factors[0][0]**(factors[0][1]+1)
    print(comparison,primes[nextprime])
    if comparison<primes[nextprime]:
        factors[0][1]=factors[0][1]*2+1
    else:
        factors.append([primes[nextprime],1])
        nextprime+=1
    count+=1
print(factors)
total=1
for factor in factors:
    total=total*(factor[0]**factor[1])
print(total)