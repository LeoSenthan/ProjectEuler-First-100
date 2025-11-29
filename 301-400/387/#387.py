def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def P387(t):
    def recursive_prime_concatenation(n, d, k):
        if d % 2 == 1 and n % 2 == 0 and n > 20:
            return
        if is_prime(n // d):
            for w in [1, 3, 7, 9]:
                m = 10 * n + w
                if is_prime(m):
                    concatenation_list.append(m)
        if k > 0:
            for j in range(10):
                m = 10 * n + j
                dm = d + j
                if m % dm == 0:
                    recursive_prime_concatenation(m, dm, k - 1)

    if t < 2:
        return 0

    concatenation_list = []
    for i in range(1, 10):
        recursive_prime_concatenation(i, i, t - 2)
    return sum(concatenation_list)

print(P387(14))
