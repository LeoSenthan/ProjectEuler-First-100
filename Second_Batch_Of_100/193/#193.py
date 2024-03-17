#All primes are square free
import math
def moebius(n):
    if n == 1:
        return 1
    p = 0
    for i in range(2, n+1):
        if n % i == 0:
            n //= i
            p += 1
            if n % i == 0:
                return 0
    return (-1) ** p

def calculate_sum(N):
    result = 0
    sqrt_N = int(math.sqrt(N))
    for k in range(1, sqrt_N + 1):
        result += math.floor(N / (k * k)) * moebius(k)
    return result

N = 2 ** 50 - 1
print(calculate_sum(N))
