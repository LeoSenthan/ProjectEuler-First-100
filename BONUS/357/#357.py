#all numbers have to be one less than a prime number
# Hence always even apart from 1 
# So n+2/2 = prime hence n/2 is odd hence number is equal to odd number *2
#Multiple of 2 not 4
#only have to check factors below half of n
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    sqrtn = int(n ** 0.5)
    for i in range(2, sqrtn + 1):
        if sieve[i]:
            sieve[2 * i::i] = [False] * (n // i - 1)
    return sieve

limit=10**8+1
prime = sieve_of_eratosthenes(limit + int(limit ** 0.5))
tab = [True] * limit
answer = 0  

for n in range(1, limit):
    if tab[n]:
        if prime[n + 1] and prime[n // 2 + 2] and all(prime[d + n // d] for d in range(3, int(n ** 0.5) + 1) if not n % d):
            answer += n
        else:
            nj2 = n
            j = 1
            while nj2 < limit:
                tab[nj2] = False
                j += 1
                nj2 = n * j * j
print(answer)
