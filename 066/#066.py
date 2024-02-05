from math import sqrt
for d in range(1,1001):
    if sqrt(d)%1!=0:
        y=0
        while True:
            y+=1
            if d*y**2-(int(sqrt(d*y**2))+1)**2==-1:
                print(int(sqrt(d*y**2))+1)
                break