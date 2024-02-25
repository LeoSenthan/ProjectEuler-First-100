def SieveOfEratosthenes(num):
    list1 = []
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            list1.append(p)
    return list1

primes = SieveOfEratosthenes(300000)

nmin = 1000000000000000
for prime in range(0, len(primes)):
    remainder, n = 0, 0
    while remainder < 10**10:
        n += 1
        remainder = ((primes[prime]-1)**prime + (primes[prime]+1)**prime) % primes[prime]**2
    if n < nmin:
        nmin = n
        print(nmin)  # Moved the print statement inside the loop
