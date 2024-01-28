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
n,nuoffactors=0,[]
while True:
    n+=1
    nuoffactors.append(len(primeFactors(n)))
    if all(factor==4 for factor in nuoffactors[-4:]):
                    print(len(nuoffactors)-3)
                    exit()
