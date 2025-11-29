def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

squares_list = [float(i**2) for i in range(1, 100)]
count = 0

for a in range(1, 101):
    for c in range(1, 101):
        for d in range(1, 101):
            for b in range(1, 101):
                if (((a+c)*(b+d) - (gcd(a, b) + gcd(b, c) + gcd(a, d) + gcd(c, d)))/2+1)**0.5%1==0:
                    count += 1
print(count)
