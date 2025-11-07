import sys
sys.set_int_max_str_digits(1000000000)

def s(n):
    return int(str(n%9)+"9" *(n//9))

def S(k):
    return sum([s(n) for n in range(1,k+1)])

curr = 1
prev = 1
count = 2
total = 0 
while count <10:
    print(S(curr)-S(prev))
    curr,prev  = curr + prev, curr