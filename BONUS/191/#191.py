from itertools import product

def generate_strings(length):
    # Define the possible characters
    options = ['0', '1', '2']
    
    # Generate all combinations of length 'length' using itertools.product
    for combination in product(options, repeat=length):
        yield ''.join(combination)

# Usage example
total = 0
# Access each string one by one
for string in generate_strings(30):
    if '222' not in string and string.count('1') < 2:
        total += 1
print(total)
