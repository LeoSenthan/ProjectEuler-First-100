from math import sqrt
possible,impossible = set(),set()
def gcd(a, b): # greatest common divisor function to check they are relatively prime to each other
    while b:
        a, b = b, a % b
    return a
for m in range(2, int(sqrt(1500001 / 2)) + 1):
    for n in range(m-1,0,-2):
        if gcd(m, n) == 1:
            s=2*m*(m+n)
            for k in range(1, 1500001 // s + 1):
                if k * s in possible:
                    impossible.add(k * s)
                else:
                    possible.add(k * s)
print(len(possible-impossible))