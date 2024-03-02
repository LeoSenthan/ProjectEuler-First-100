from math import factorial
total=0
for n in range(1,1000000):
    chain,repeats,current=0,[],n
    while current not in repeats:
        repeats.append(current)
        temp=current
        current,chain=0,chain+1
        for digit in str(temp):
            current=current+factorial(int(digit))
    if chain==60:
        total+=1
print(total)   