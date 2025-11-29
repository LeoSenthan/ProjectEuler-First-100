#How many numbers are one directional below 
#1000 = 474 Non - Bouncy
#10000 = 1674
#100000 = 4953
#1000000 = 12951 
# 10**7 =30816
# 10**8 = 67986
# 10**9 = 140906
# 10**10 = 277032
def Increasing(number):
    for i in range(0,len(number)-1):
        if int(number[i])<=int(number[i+1]):
            pass
        else:
            return False
    return True

def Decreasing(number):
    for i in range(0,len(number)-1):
        if int(number[i])>=int(number[i+1]):
            pass
        else:
            return False
    return True

x=2
count=0
for i in range(1,10**x):
    if Increasing(str(i)):
        count+=1
    else:
        if Decreasing(str(i)):
            count+=1
print(count)

from math import factorial

def choose(n,p):
    return factorial(n)/(factorial(p)*factorial(n-p))
print(choose(110,100)+choose(109,100)-(100*10+2))
