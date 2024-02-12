from math import sqrt

l, odd_period = 10000, 0

for num in range(2,l+1):
    r=limit=int(sqrt(num))
    if limit**2==num: continue
    z, period = 1, 0
    while z !=1 or period == 0:
        z=(num - r * r)//z
        r=(limit + r)//z*z-r
        period += 1
    if period % 2 == 1: odd_period += 1
print (odd_period)