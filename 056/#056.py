maxsum=0
for a in range(1,100):
    for b in range(1,100):
        sum=0
        for digit in str(a**b):
            sum+=int(digit)
        maxsum=sum if sum>maxsum else maxsum
print(maxsum)