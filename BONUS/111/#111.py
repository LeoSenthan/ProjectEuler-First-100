import math
def primeFactors(n):
  factors=[]
  while n % 2 == 0:
      factors.append(2)
      n = n // 2
  for i in range(3,int(math.sqrt(n))+1,2):
      while n % i== 0:
          factors.append(i)
          n = n // i
  if n > 2:
      factors.append(n)
  return len(factors)
print(primeFactors(2))
from itertools import permutations
for i in range(0,10):
    x=10
    while True:
        x-=1
        current=["1"]*x+[str(i)]
        perms=list(set(permutations(current)))
        for i in perms:
            current=int(str(i).replace(", ","").replace("'","")[1:-1])
            if primeFactors(current)==1:
                total=0