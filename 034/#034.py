#Max value of 1 digit is 9 factorial which is 362880 hence max is 7 digits which is 2540160
total=0
from math import factorial
for n in range(1,2540161):
    currenttotal=0
    digits=str(n)
    for digit in digits:
        currenttotal=currenttotal+factorial(int(digit))
    if currenttotal==n:
        total=total+n
print(total-1-2) # Subtract 3 since 1 and 2 do not count
