from Euler import gcd, sqrt
L = 1500001
maybe = set()
nope = set()
for m in xrange(2, int(sqrt(L/2))):
    for n in xrange(m-1, 0, -2):
        if gcd(m, n) == 1:
            s = 2*(m*m + m*n)
            for k in xrange(1, L/s+1):
				nope.add(k*s) if k*s in maybe else maybe.add(k*s)
print len(maybe-nope)