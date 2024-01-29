"""
from itertools import permutations
n=0
while True:
    n+=1
    perms,count=permutations(sorted(str(n**3))),0
    for cubecheck in perms:
        cubecheck,format=list(cubecheck),""
        for digit in cubecheck:
            format+=digit
        if (int(format)**(1/3))%1==0:
            count+=1
    if count==5:
        print(n**3)
        break
"""
#Way Too Slow Estimate Below 20000
cubes=[]
for n in range(1,20000):
    cubes.append(sorted(str(n**3)))
for cube in cubes:
    if cubes.count(cube)==5:
        print((cubes.index(cube))**3)
        break