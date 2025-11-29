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
  return list(set(factors))

count=0
for d in range(4,12001):
    denomfact=primeFactors(d)
    for n in range(d//3+1,d//2+1):
        numfact=primeFactors(n)
        if (set(numfact) - set(denomfact))==set(numfact):
            count+=1
print(count)