#Can not have a 2,4,5,6,8,0 so must be made of 1,3,7,9
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

count,total=0,0
primes=SieveOfEratosthenes(1000000)
for prime in primes:
    left,right=str(prime),str(prime)
    Flag=True
    for digit in range(0,len(str(prime))-1):
        left=left[1:]
        right=right[:-1]
        if int(left) in primes and int(right) in primes:
            pass
        else:
            Flag=False
            break
    if Flag==True:
        count+=1
        total+=prime
        if count==15: # Since 2,3,5,7 do not count
            print(total-2-3-5-7)
            exit()