def euler_totient(n):
    if n < 1:
        return 0
    
    phi = n  # Initialize phi to n    
    # Check for divisibility by each prime number up to sqrt(n)
    p = 2
    while p * p <= n:
        if n % p == 0:  # If p divides n
            while n % p == 0:
                n //= p
            phi -= phi // p
        p += 1
    
    if n > 1:  # If n is a prime number greater than 1
        phi -= phi // n
    return phi

def compute_totient_range(limit):
    phi = list(range(limit + 1))  # Initialize an array for phi values
    
    for i in range(2, limit + 1):
        if phi[i] == i:  # If i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    
    return phi

def SieveOfEratosthenes(num):
  list1=[]
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
primes=SieveOfEratosthenes(40000000)

total=0
# Example usage
result=compute_totient_range(40000000)  # Output: [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
for prime in primes:
    current=result[prime]
    chain=1
    while True:
        current=result[current]
        chain+=1
        if current==1:
            break
    if chain==25:
        total+=prime
print(total)
