def SieveOfEratosthenes(num):
    primes = []
    prime = [True] * (num+1)
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            primes.append(p)
    return primes
from math import factorial
# Generate prime numbers
primes = SieveOfEratosthenes(10**8)[2:]
total = 0
# Precompute factorial(p-5) for each prime p
factorial_cache = {}
for p in primes:
    factorial_cache[p] = factorial(p-5)
# Optimized calculation
for p in primes:
    total += (factorial_cache[p]*9)%p
print(total)
