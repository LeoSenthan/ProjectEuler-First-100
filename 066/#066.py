from math import isqrt
for d in range(1,1001):
    if isqrt(d)==True:
        y=0
        while True:
            y+=1
            if d*y**2-(int(sqrt(d*y**2))+1)**2==-1:
                print(int(sqrt(d*y**2))+1)
                break