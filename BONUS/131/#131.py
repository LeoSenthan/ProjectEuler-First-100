#p must be difference of cubes as n**3+n**2*p=n**2(n+p)
#only difference of consecutive cubes can be prime
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

count=0
cubes=[1,8]
n=2
differences=[7]
while differences[-1]<1000000:
    if primeFactors(differences[-1])==1:
        count+=1
    n+=1
    cubes.append(n**3)
    differences.append(cubes[-1]-cubes[-2])
print(count)