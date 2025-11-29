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
primes=SieveOfEratosthenes(100000)

def order(a, m):
    if a == 0 or m <= 1:
        return 0
    result = 1
    b = a % m
    while b != 1:
        b = (b * a) % m
        result += 1
    return result
def remove(a, b):
    """Remove factors of 'b' from 'a'."""
    while a % b == 0:
        a //= b
    return a
def remove52(n):
    """Remove factors of 2 and 5 from 'n'."""
    n = remove(n, 2)
    n = remove(n, 5)
    return n
# Remove 2 and 5 factors from the order of each prime
filtered_primes = [p for p in primes if remove52(order(10, p)) != 1]

# Calculate and print the solution
solution = 2 + 3 + 5 + sum(filtered_primes)
print("Solution is:", solution)
