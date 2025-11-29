#Length of both subsets are equal
#Hence subsets are of length 1-6
#Number of trivially unequal for 1 =0 
# 2 = 1 
#3 = 5
#4 = 21
#5 = 84
#6 = 330
#Number of ways to make subsets of size 1-6 is 12C2 + 12C4 + 12C6 + 12C8 +12C10 and 12C12
from math import factorial
def choose(a,b):
    return (factorial(a)/(factorial(b)*factorial(a-b)))

print(choose(12,2)*0+choose(12,4)*1+choose(12,6)*5+choose(12,8)*21+choose(12,10)*84+choose(12,12)*330)