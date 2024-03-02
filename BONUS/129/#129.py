from math import gcd
def repunit_sum(k):
    return (10**k - 1) // 9
def A(n):
    remainder,k = 1,1
    while remainder != 0:
        k+=1
        remainder=(remainder * 10 + 1)%n
    return k

n = 10**6
while True:
    n += 1
    if gcd(n, 10) == 1:
        if A(n) > 10**6:
            print(n)
            break
