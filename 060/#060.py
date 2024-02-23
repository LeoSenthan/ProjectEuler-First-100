import itertools as iter 

set_size = 5

def prime_sieve(num):
    primes = []
    sieve = [True] * (num + 1)
    for p in range(2, int(num ** 0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, num + 1, p):
                sieve[i] = False
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = prime_sieve(10000)

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain + [p]):
            new_chain = make_chain(chain + [p])
            if new_chain:
                return new_chain
    return False

def all_prime(chain):
    return all(is_prime(int(str(p[0]) + str(p[1]))) for p in iter.permutations(chain, 2))

chain = make_chain([primes.pop(0)])

if chain:
    print("Project Euler 60 Solution =", sum(chain), chain)
else:
    print("No solution found.")
