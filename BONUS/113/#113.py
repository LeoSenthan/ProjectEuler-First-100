count = 0
for n in range(1, 10**7):
    n = str(n)
    increasing = True
    decreasing = True
    for char in range(len(n)-1):
        if int(n[char]) < int(n[char+1]):
            decreasing = False
        elif int(n[char]) > int(n[char+1]):
            increasing = False
    
    if increasing or decreasing:
        count += 1
#10**1 = 9 10**2=99 10**3=474 10**1674 10**5=4953 10**6=12951 10**7= 10**8 10**9 10**10
print(count)
