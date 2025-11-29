def SieveOfEratosthenes(num):
    list1 = []
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            list1.append(p)
    return list1
prime=[0]+SieveOfEratosthenes(1000000)
n=1
#remainder maximum = 2*n*prime[n]
while 2*n*prime[n]<10**10:
    n+=2
print(n)