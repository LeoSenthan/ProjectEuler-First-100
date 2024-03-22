from math import factorial
n=100000001
total=0
for i in range(2,n):
    n=2
    while factorial(n)%i!=0:
        n+=1
    total+=n
print(total)