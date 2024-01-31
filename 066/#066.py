#x**2-D*y**2=1
#x**2=1+D*y**2
#x**2-1/D=y**2
#sqrt ((x**2-1)/D)=y
#check only prime numbers
max,dval=0,0
from math import sqrt

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
primes=SieveOfEratosthenes(1000)

#Chakravala Method
def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
 
    while k != 1 or y == 0:
        p=k*(p/k+1)-p
        p-=int((p-sd)/k)*k
        x=(p*x1 + d*y)/abs(k)
        y=(p*y+x1)/abs(k)
        k=(p*p-d)/k
        x1=x
    return x
for d in primes[5:]:
    print(d)
    if sqrt(d)%1!=0:
        x=pell(d)
        if x>max:
            max,dval=x,d
print(dval)
9*8*7*6