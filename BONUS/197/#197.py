#f(x)=math.floor(2**(30.403243784-x**2))*10**-9
import math
current,n=-1,0
while n<10**4:
    n+=1
    current=math.floor(2**(30.403243784-current**2))*10**-9
    print(current)
#Results keep switching hence 
print(current+math.floor(2**(30.403243784-current**2))*10**-9)