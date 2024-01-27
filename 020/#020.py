from math import factorial
digits,total=str(factorial(100)),0
for digit in digits:
    total+=int(digit)
print(total)