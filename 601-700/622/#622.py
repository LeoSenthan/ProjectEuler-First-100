def generate_divisors(index, current_divisor, prime_factors, divisors):
    # Base case: if we've processed all prime factors
    if index == len(prime_factors):
        divisors.append(current_divisor)
        return
    
    # Recursively generate divisors for current prime factor
    for i in range(prime_factors[index][0] + 1):
        generate_divisors(index + 1, current_divisor, prime_factors, divisors)
        current_divisor *= prime_factors[index][1]

def find_divisors(n):
    prime_factors = []
    
    # Factorize n to find all prime factors and their powers
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            prime_factors.append([count, i])
        i += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        prime_factors.append([1, n])
    
    # Start generating divisors from the prime factors
    divisors = []
    generate_divisors(0, 1, prime_factors, divisors)
    return divisors

# Calculate n and find its divisors
n = (2**60)-1
total=0
divisors = find_divisors(n)
divisorsofsixty=find_divisors(60)[:-1]
print(divisors)
for divisor in divisors:
    if 2**60%divisor==1:
        flag=True
        for divisorofsixty in divisorsofsixty:
            if (2**divisorofsixty%divisor)==1:
                flag=False
        if flag==True:
            total+=(divisor+1)
print(total)