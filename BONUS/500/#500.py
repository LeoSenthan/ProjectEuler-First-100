#2**0=1
#2**1=2
#2**2=6
#2**3=24
#2**5=120
#Pattern is times 3 times 4 times 5
multiplier=1
start=1
for i in range(0,500500):
    multiplier+=1
    start*=multiplier
print(start%500500507)