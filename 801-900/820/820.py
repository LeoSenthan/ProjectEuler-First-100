
def d_n_over_k(n, k):
    return (10 * pow(10, n - 1, k)) // k


def S(limit):
    total = 0
    n_minus_1 = limit - 1
    for k in range(1, limit + 1):
        total += (10 * pow(10, n_minus_1, k)) // k
    return total


print(S(10**7))