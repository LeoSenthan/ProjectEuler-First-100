#Recurring digits have to be 3 or 5 appearances since 2 or 4 will result in multiple of 3 so most likely is 3 of  same digit
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

for prime in primes:
    if prime>1000:
        Flag,checker=False,sorted(str(prime))
        for digit in checker:
            if checker.count(digit)==3:
                replacement,Flag=digit,True
        if Flag==True:
            count=0
            for newdigit in "0123456789":
                combo=str(prime).replace(replacement,newdigit)
                if int(combo) in primes and len(str(int(combo)))==len(str(prime)):
                    count+=1
            if count==8:
                print(prime)
                exit()