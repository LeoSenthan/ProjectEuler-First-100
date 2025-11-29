def compute_lpf(n):
    lpf = [0] * (n + 1)
    for i in range(2, n + 1):
        if lpf[i] == 0:  # i is prime
            for j in range(i, n + 1, i):
                lpf[j] = i
    return lpf

def S(N):
    lpf = compute_lpf(N)
    total = 0
    for i in range(2, N + 1):
        count = 0
        x = i
        p = lpf[i]
        while x % p == 0:
            count += 1
            x //= p
        total += p * count
    return total

print(S(10**8))  # Fast even for large N
