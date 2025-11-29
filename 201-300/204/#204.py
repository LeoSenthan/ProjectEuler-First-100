primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def doIt(setin,mul):
    s = set()
    for y in setin:
        z = y
        while z <10**9:
            s.add(z)
            z*=mul
    return s
s=set()
s.add(1)
for prime in primes:
    s = doIt(s,prime)
print (len(s))