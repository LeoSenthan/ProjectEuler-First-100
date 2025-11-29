#multiple the log(base)*exponent
from math import log10
with open("099/#099.txt") as f:
    numbers=f.readlines()
max,line=0,-1
for pair in range(0,len(numbers)):
    pairs=numbers[pair].split(",")
    if log10(int(pairs[0]))*int(pairs[1])>max:
        max,line=log10(int(pairs[0]))*int(pairs[1]),pair
print(line)
#It is 709 since list index starts with 0