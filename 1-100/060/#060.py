from copy import copy
from math import sqrt
primes,concatmem = [2,3,5,7,11,13],{}

def nextprime():
    next_num = primes[-1] + 2
    nnsqrt = int(sqrt(next_num))
    isprime = False
    while not isprime:
        isprime = True
        for prime in primes:
            if prime > nnsqrt: break
            if next_num % prime == 0:
                next_num += 2
                isprime = False
                break
    primes.append(next_num)
    return next_num
def is_prime(num):
    if num < 2:
        return False
    nsqrt = int(sqrt(num))
    if num == nsqrt * nsqrt: return False
    last_prime = primes[-1]
    while last_prime < nsqrt:
        last_prime = nextprime()
    for prime in primes:
        if prime > nsqrt: break
        if num % prime == 0: return False
    return True
def concat2(a, b):
    key_pair = (a, b)
    if key_pair in concatmem: return concatmem[key_pair]
    stra = str(a)
    strb = str(b)
    result = is_prime(int(stra + strb)) \
         and is_prime(int(strb + stra))
    concatmem[key_pair] = result
    return result
def concat(set, lvl):
    for i in range(lvl):
        if not concat2(set[i], set[lvl]): return False
    return True
def find_set():
    min_sum_start = 999999999
    min_sum = min_sum_start
    i = 4
    set = [0, 0, 0, 0, 0]
    while True:
        i += 1
        set[0] = primes[i]
        for j in range(i-1,3,-1):
            set[1] = primes[j]
            if not concat(set,1): continue
            for k in range(j-1,2,-1):
                set[2] =primes[k]
                if not concat(set, 2): continue
                for l in range(k - 1, 1, -1):
                    set[3]=primes[l]
                    if not concat(set, 3): continue
                    for m in range(l - 1, 0, -1):
                        set[4]=primes[m]
                        if not concat(set, 4): continue
                        sum_set=sum(set)
                        if min_sum > sum_set:
                            min_sum,min_set = sum_set,copy(set)
        if min_sum < min_sum_start: return min_sum, min_set

sum_of_set, set = find_set()
print(sum_of_set, set)