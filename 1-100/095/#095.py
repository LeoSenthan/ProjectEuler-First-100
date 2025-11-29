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
chainlength,lowest=0,100000000000
for n in range(2,1000001):
    chain=[]
    current=n
    Flag=True
    while True:
        chain.append(current)
        factors=primeFactors(current)
        if (sum_of_divisors(factors)-current)==n:
            break
        elif (sum_of_divisors(factors)-current)>1000000 or (sum_of_divisors(factors)-current)==1 or (sum_of_divisors(factors)-current) in chain:
            Flag=False
            break
        current=sum_of_divisors(factors)-current
    if Flag==True:
        if len(chain)>=chainlength:
            print(chain)
            print(n,len(chain))
            chainlength=len(chain)
            chain=sorted(chain)
            if chain[-1]<lowest:
                lowest=chain[-1]
print(chainlength)
#Highest chain length is 28 hence answer is 14316