def power_modulo(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def remainder_large_number_single_digit(base, exponent, modulus):
    # Compute the remainder of the base
    base_remainder = base % modulus
    # Compute the remainder of 10^exponent
    exponent_remainder = power_modulo(10, exponent, modulus)
    # Compute the final remainder
    remainder = (base_remainder * exponent_remainder) % modulus
    return remainder

# Initialize total
total = 0
fibbonaci=[1,1]
while len(fibbonaci)<90:
    fibbonaci.append(fibbonaci[-1]+fibbonaci[-2])
# Iterate over the range
for i in fibbonaci[1:]:
    if i // 9 < 1:
        total += i
    else:
        # Calculate the remainder using modular arithmetic
        remainder = remainder_large_number_single_digit(i % 9 + 1, i // 9, 1000000007)
        # Add to total
        total += remainder-1

print(total %1000000007)
