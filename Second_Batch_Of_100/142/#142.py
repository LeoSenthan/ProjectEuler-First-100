#x>y>z>0
#x+y = a
#x-y = b
#x+z = c
#x-z = d
#y+z = e
#y-z = f
#2x=a**2+b**2
#x=1/2(a+b)
#a=x+y
#Hence y is directly affected by x
# a-b/2>y>z and a=x+y
from math import sqrt
for a in range(1,10000000):
    a=a**2
    b=a
    x=0.5*(a+b)
    y=(a-x)
    if x.is_integer() and y.is_integer():
        for z in range(1,int(y)):
            if sqrt(y-z).is_integer() and sqrt(y+z).is_integer and sqrt(x-z).is_integer and sqrt(x+z).is_integer:
                print(x,y,z)
                exit()
