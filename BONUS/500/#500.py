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
factors=[[2,3,16],[3,1,9],[5,1,25]]
nextprime=3
while count<500500:
    optimal=1000000000000000000000000000000000000000
    Flag=True
    for factor in range(0,len(factors)):
        if factors[factor][2]<primes[nextprime] and factors[factor][2]<optimal:
            optimal=factors[factor][2]
            next=factor
            Flag=False
    if Flag==True:
        factors.append([primes[nextprime],1,primes[nextprime]**3])
        nextprime+=1
    else:
        factors[next][1]=factors[next][1]*2+1
        factors[next][2]=factors[next][0]**(factors[next][1]+1)
    count+=1      
total=1
for factor in factors:
    total=total*(factor[0]**factor[1])
print(total%500500507)