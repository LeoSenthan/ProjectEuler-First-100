from math import factorial
def F(n):
    return factorial(n)
def C(n, r):
    return F(n)/(F(r) * F(n-r))
def numbers(go1, go2, go3, n = 10):
    length = go1 + go2*2 + go3*3
    if go3 > 0:
        return C(length, 3) * n * numbers(go1, go2, go3-1, n-1) / go3
    elif go2 > 0:
        return C(length, 2) * n * numbers(go1, go2-1, go3, n-1) / go2
    elif go1 > 0:
        return C(length, 1) * n * numbers(go1-1, go2, go3, n-1) / go1
    return 1

count = 0
for go3 in range(10):
    for go2 in range(10):
        go1 = 18 - go2*2 - go3*3
        if go1 >= 0 and go1 + go2 + go3 <= 10:
            count = count + numbers(go1, go2, go3)
print (count * 9 / 10)