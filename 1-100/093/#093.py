from operator import add, sub, mul, truediv
import itertools

def seq_length(s, c=1):
    # Calculate the length of a sequence until a missing number is found
    while c in s: 
        c += 1
    return c - 1
maxt, maxs = 0, 0

# Iterate over all combinations of 4 numbers from 1 to 9
for terms in itertools.combinations(range(1, 10), 4):
    s = set()
    # Iterate over all permutations of the 4 chosen numbers
    for n in itertools.permutations(terms):
        # Iterate over all possible combinations of arithmetic operations
        for op in itertools.product([add, mul, sub, truediv], repeat=3):
            # Calculate (a.b).(c.d)
            x = op[0](op[1](n[0], n[1]), op[2](n[2], n[3]))
            if x % 1 == 0 and x > 0: 
                s.add(int(x))   
            # Calculate ((a.b).c).d
            x = op[0](op[1](op[2](n[0], n[1]), n[2]), n[3])
            if x % 1 == 0 and x > 0: 
                s.add(int(x))
        # Update the maximum sequence length found so far
        if seq_length(s) > maxs: 
            maxs, maxt = seq_length(s), terms
# Print the numbers that produce the longest sequence
print(''.join(str(i) for i in maxt))
