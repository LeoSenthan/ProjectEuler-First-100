import math
# a + b = c + d + 1
def factors(n):
    found = -1
    for ix in range(int(math.sqrt(n)), -1,-1):
        if n % ix == 0:
            if found == -1:
                found = ix + n // ix
            else:
                if abs(found - (ix + n // ix)) == 1:
                    return True
                return False

def total(power):
    count = 0
    for ix in range(4,10**power,4):
        if factors(ix):
            count += 1
    print(count)

total(2)
total(3)
total(4)
total(5)
total(6)
# 84 2 2 3 7
# 6 14, 7, 12