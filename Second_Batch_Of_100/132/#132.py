def repunit_sum(k):
    return (10**k - 1) // 9
# one of the factors is 11 as the difference between odd digits and even digits are 0

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

factors=primeFactors(repunit_sum(13))
print(factors)
#r(3)=3, 37
#R(4)= 11,101
#R(5) = 41 *271
#R(6) = 3 * 7 * 11 * 13 *37
#R(7) = 239*4649
#R(8) = 11 73 101 137
#R(9) = 3 3 37 333667
#R(10) = 11 41 271 9091
#r(11) = 21649 513239
#r(12) = 3,7,11,13,101,9901
#r(13) = 53,79,265371653
# First factor is not 2,3,5 could be 7
#Has to be 11 as on even k lengths 11 is a power
#After dividing by 11 the number now becomes 101010... with the same length -1 ends in a 1
#Factorized = 11*int(str(1)+"01"*10**9/2-1)