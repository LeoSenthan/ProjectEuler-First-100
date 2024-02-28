def SieveOfEratosthenes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if prime[p]]
def count_primes(limit):
    primes = SieveOfEratosthenes(limit)
    total = 0
    for k in range(len(primes)):
        n_over_kth_prime = limit // primes[k]
        count = sum(1 for p in primes if p <= n_over_kth_prime)
        if count > k:
            count = k
        total += count
    return total
result = count_primes(10**8)
print(result)