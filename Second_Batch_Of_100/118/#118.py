import itertools
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Step 1: Generate all prime numbers made from unique subsets of digits 1–9
all_digits = "123456789"
primes = []

for i in range(1, 10):  # lengths 1 to 9
    for p in itertools.permutations(all_digits, i):
        num_str = ''.join(p)
        num = int(num_str)
        if is_prime(num):
            primes.append((num_str, set(p)))  # store both the string and its digit set

# Step 2: Recursive backtracking to find unique partitions
unique_partitions = set()

def recursive_check(remaining_digits, path):
    if not remaining_digits:
        # Sort the path to normalize equivalent permutations
        partition_key = tuple(sorted(path))
        unique_partitions.add(partition_key)
        return
    for prime_str, digit_set in primes:
        if digit_set.issubset(remaining_digits):
            recursive_check(remaining_digits - digit_set, path + [prime_str])

# Start with all digits available
recursive_check(set(all_digits), [])

# Final output
print("Total unique partitions:", len(unique_partitions))
