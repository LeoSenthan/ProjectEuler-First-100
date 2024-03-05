from itertools import product

def generate_strings(length):
    options = ['0', '1', '2']    
    for combination in product(options, repeat=length):
        yield ''.join(combination)

total = 0
for string in generate_strings(30):
    if '222' not in string and string.count('1') < 2:
        total += 1
print(total)
