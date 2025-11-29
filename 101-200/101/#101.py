def highest_order_term(seq):
    order = 0
    order_factorial = 1
    while any(t != seq[0] for t in seq):
        # Take the difference until all the terms are the same.
        seq = [(i2 - i1) for i1, i2 in zip(seq, seq[1:])]
        order += 1
        order_factorial *= order
    return seq[0] / order_factorial, order

def make_poly(seq):
    terms = []  # List to store (K, o) pairs
    while True:
        K, o = highest_order_term(seq)
        terms.append((K, o))
        if o == 0:
            break  # All terms have been obtained.
        # Subtract Kn^o from each term
        diff = [K * (n ** o) for n in range(1, len(seq))]
        seq = [a - b for a, b in zip(seq, diff)]
    return lambda n: sum(k * (n ** o) for k, o in terms)

def t(n): 
    return sum((-n) ** e for e in range(11))
seq = [t(n) for n in range(1, 20)]

result = sum(make_poly(seq[:i])(i + 1) for i in range(1, 11))
print("Sum of polynomial interpolation:", result)
