#Sieve of Eratosthenes
def SieveOfEratosthenes(num):
  list1=[]
  prime = [True for i in range(num+1)]
  p=2
  while (p*p <= num):
      if (prime[p] == True):
          for i in range(p*p,num+1,p):
              prime[i] = False
      p+=1
  for p in range(2,num+1):
      if prime[p]:
          list1.append(p)
  return list1

count=0
primes=SieveOfEratosthenes(1000000)
for prime in primes:
    if ("2" or "4" or "6" or "8" or "0" or "5") in str(prime):
        pass
    else:
        Flag,string=True,str(prime)
        for rotate in range(0,len(string)):
            primerotate=int(string[rotate:]+string[:rotate])
            if primerotate in primes:
                pass
            else:
                Flag=False
        if Flag==True:
            count+=1
print(count+1)