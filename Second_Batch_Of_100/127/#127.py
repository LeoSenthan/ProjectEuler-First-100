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
  return factors
factors=primeFactors(64)

def rad(n):
    unique=list(set(primeFactors(n)))
    result=1
    for i in unique:
        result*=i
    return result
rads=[0]
for i in range(1,100000):
    rads.append(rad(i))

def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True
    return False
total=0
for c in range(3,1000):
    for b in range(1,c//2):
        if euclidean_algorithm(b,c-b):
                    if rads[c]*rads[b]*rads[c-b]<c:
                        total+=c
print(total)
                
