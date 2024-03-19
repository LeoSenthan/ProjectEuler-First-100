#120 = 5! = 16
#1! = 1
#2! = 2
#3! = 4
#4! = 8
#5! = 16
#2**1 divisors = 2!
# 2**500500 divisors = 5005001!
from math import factorial
print(factorial(500501)%500500507)