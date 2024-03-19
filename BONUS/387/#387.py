#just add  a digit to existing harshad numbers to create  new harshad number until it is 14 digits long
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
  return True if len(factors)==1 else False

digits=[1]
harshad=["2","3","5","7"]
total=sum(int(i) for i in harshad)
print(total)
count=0
while count<10:
    count+=1
    digits=[]
    for number in harshad:
        for digit in range(0,10):
            current=number+str(digit)
            digitsum=sum(int(char) for char in current)
            if primeFactors(int(current)/digitsum):
                digits.append(current)
    harshad=digits
    total+=sum(int(i) for i in harshad)
    print(total)