
def L(n):
    total=0
    for i in range(1,n//4+4):
        for j in range(1,i):
            if i**2-j**2 <n:
                break
            if i**2-j**2 == n:
                total+=1

    return total

print(L(32))

def N(n):
    total=0
    for i in range(1,100000):
        if L(i) == n:
            total+=1
    return N(n)
print(N(15))