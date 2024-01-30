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
          list1.append(str(p))
  return list1
primes=SieveOfEratosthenes(20000)
ultimateset=[]
for prime in range(0,len(primes)):
    primepair=[int(primes[prime])]
    for biggerprime in range(prime+1,len(primes)): 
        if primes[prime]+primes[biggerprime]==(primes[prime]+primes[biggerprime])[::-1]:
            primepair.append(int(primes[biggerprime]))
    if len(primepair)>=5:
        ultimateset.append(primepair)
finalset=[]
for i in range(0,len(ultimateset)):
    actual=[]
    for prime in range(0,len(ultimateset[i])):
        for z in range(0,len(ultimateset)):
            if ultimateset[i][prime] in ultimateset[z]: 
                actual.append(ultimateset[i][prime])
                break
    finalset.append(actual)
supremeset=[]
for i in range(0,len(finalset)):
    count=2
    for x in range(0,len(finalset)):
        if finalset[i][0] in finalset[x]:
            count+=1
    if count>=5:
        supremeset.append(finalset[i])
for i in supremeset:
    if len(i)==5:
        print(sum(i))