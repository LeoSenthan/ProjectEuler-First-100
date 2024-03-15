def factor_pairs(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def find_solutions(n):
    count=0
    pairs = factor_pairs(n)
    for pair in pairs:
        a, b = pair
        x = (a + b) // 2
        y = (a - b) // 2

        if x**2 - y**2 == n:
            count+=1
    return count

answer=0
for n in range(1,100001):
    if find_solutions(n)==15:
        answer+=1
print(answer)