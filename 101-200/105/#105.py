def has_common_bit_set(n, m, dim):
    """Check if there is any common bit set to 1 in two integers."""
    for _ in range(dim):
        if n & 1 == 1 and m & 1 == 1:
            return True
        n >>= 1
        m >>= 1
    return False

def count_set_bits(n, m, dim):
    """Count the number of set bits in each number."""
    nn = nm = 0
    for _ in range(dim):
        if n & 1 == 1:
            nn += 1
        if m & 1 == 1:
            nm += 1
        n >>= 1
        m >>= 1
    if nn > nm:
        return 1
    elif nn == nm:
        return 0
    else:
        return -1

def binary_sum(a, m):
    """Calculate the sum of elements in 'a' based on the binary representation 'm'."""
    total = 0
    for i, value in enumerate(a):
        if m & 1 == 1:
            total += value
        m >>= 1
    return total

def total_sum(a):
    """Calculate the total sum of elements in 'a'."""
    return sum(a)

def generate_all_sums(a):
    """Generate all possible subsets of array 'a' and calculate their sums."""
    subset_sums = []
    for i in range(1 << len(a)):
        subset_sums.append(binary_sum(a, i))
    return subset_sums

def is_valid_subset(subset_sums, dim):
    """Check if the generated subsets are valid."""
    for i, value in enumerate(subset_sums):
        try:
            index = subset_sums.index(value, i+1)
            if index != -1:
                return False
        except ValueError:
            pass

    for i in range(len(subset_sums)):
        for j in range(i+1, len(subset_sums)):
            if not has_common_bit_set(i, j, dim):
                if subset_sums[i] == subset_sums[j]:
                    return False
                if (subset_sums[i] < subset_sums[j] and count_set_bits(i, j, dim) == 1) or \
                   (subset_sums[j] < subset_sums[i] and count_set_bits(i, j, dim) == -1):
                    return False
    return True

sets, answer = [], 0
with open("Second_Batch_Of_100/105/#105.txt", "r") as file:
    for line in file:
        sets.append(list(map(int, line.strip().split(','))))

for s in sets:
    s.sort()
    subset_sums = generate_all_sums(s)
    if is_valid_subset(subset_sums, len(s)):
        answer += total_sum(s)

print(answer)
