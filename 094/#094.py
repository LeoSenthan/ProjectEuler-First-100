#possibilities are 3,3,4 or 4,3,3 hence 2 for each value of n
from math import sqrt
def HeronFormula(a,b,c):
    s=(a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

n,perimeter,count=1,0,0
while perimeter<1000000000:
    n+=1
    checkbottom=HeronFormula(n,n,n-1)
    checktop=HeronFormula(n,n,n+1)
    if checkbottom%1==0:
        count+=1
    if checktop%1==0:
        count+=1
    perimeter=n*3-1
print(count)


