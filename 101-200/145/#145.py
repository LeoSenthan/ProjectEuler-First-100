#120 is equal to less than 1000
#Brute Force For when limit is 10**4 and 10**5 to try and work out a pattern as 10**4 = 720 and 10**5 = 720 10**6=18720
count = 0
for n in range(2,10):
    if n % 2 == 0:
         count += 20 *30**(n//2 - 1)
    elif n % 4 == 3:
         count += 100 *500**(n//4)
print(count)