import itertools,math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


combined=[]
prev="', "
new="   "
for i in range(1,10):
    object=itertools.permutations(list("123456789"),i)
    combined=itertools.chain(combined,object)
primes=[]
for perm in list(combined):
    perm=(int(str(perm)[1:-1].translate(str.maketrans(prev,new)).replace(" ","")))
    if is_prime(perm):
        primes.append(perm)
print(len(primes))
