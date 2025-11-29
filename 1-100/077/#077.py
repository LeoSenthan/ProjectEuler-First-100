primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79] # Sequence 
#The On-Line Encyclopedia of Integer Sequences!)
#A000607 Number of partitions of n into prime parts.
target = 11
#Reused code from 76
while True:
    ways = [1] + [0]*target # Keep initializing list for different target values 
    for prime in primes:
        for i in range(prime, target+1):
            ways[i] += ways[i-prime]
    if ways[target] > 5000: 
        break    
    target+=1
print(target)