n =[0]+[1]*(10**7)
for every in range(2,10**7+1):
    for num in range(every,10**7+1, every):
        n[num]+=1
# Count the number of consecutive elements with the same value
score = sum(1 for num in range(10**7) if n[num] == n[num + 1])
print(score)