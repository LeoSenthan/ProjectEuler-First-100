pairs=[0,0]
for n in range(2,10):
    total=0
    for factor in range(1,n):
        if n%factor==0:
            total+=factor
    pairs.append(factor)
print(pairs)