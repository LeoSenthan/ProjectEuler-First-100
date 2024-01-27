pairs=[0,0]
for n in range(2,10000):
    total=0
    for factor in range(1,n//2+1):
        if n%factor==0:
            total+=factor
    pairs.append(total)
total=0
for n in range(0,len(pairs)):
    if pairs[n]<len(pairs)-1:
        if n==pairs[pairs[n]] and n!=pairs[n]:
            total=total+n+pairs[pairs[n]]
            print(pairs[n],n)
print(int(total/2))