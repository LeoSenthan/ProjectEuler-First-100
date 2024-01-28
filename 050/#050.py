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
maxcount, answer = 0,0
for lowest in range(0,len(primes)):
    total,count=primes[lowest],1
    for next in range(lowest+1,len(primes)):
        total,count =total+primes[next],count+1
        if total in primes:
            if count>maxcount:
                maxcount,answer =count,total
print(answer)
