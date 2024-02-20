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

def sum_of_divisors(factors):
    total,unique=1,list(set(factors))
    for factor in unique:
        minisum=1
        for power in range(1,factors.count(factor)+1):
            minisum+=factor**power
        total=total*minisum
    #Includes Itself
    return total
chainlength=0
for n in range(2,1000001):
    print(n)
    chain=[]
    current=n
    Flag=True
    while True:
        chain.append(current)
        factors=primeFactors(current)
        print(sum_of_divisors(factors)-current)
        if (sum_of_divisors(factors)-current)==n:
            break
        elif (sum_of_divisors(factors)-current)>1000000 or (sum_of_divisors(factors)-current)==1:
            Flag=False
            break
        current=sum_of_divisors(factors)-current
    if Flag==True:
        if len(chain)>=chainlength:
            print(chain)
            chainlength=len(chain)
            chain=sorted(chain)
            print(chain[0])
print(chainlength)