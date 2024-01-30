#probability of 2 blue is b/total * b-1/total-1 ==1/2
#2b(b-1)=total(total-1)
#2b**2-2b-total(total-1)=0 # quadratic formula a=2 b=-2 c=-total(total-1)
#Solve to find b where b is a positive whole number
total=1000000000000
from math import sqrt
while True:
    try:
        firstsolution=(-2+sqrt(4+8*(total*(total-1))))/4
    except:
        firstsolution=-100
    if firstsolution%1==0 and firstsolution>0:
        if (firstsolution*(firstsolution-1))/(total*(total-1))==0.5:
            print(firstsolution)
            break
    total+=1
