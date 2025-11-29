from math import sqrt
count=0
for a in range(1, 500000):
      count += int(sqrt(a ** 2 + 1000000) - a) // 2
print(count)
# Number of solutions for a given outer length of x is equal to (tiles/4)//x