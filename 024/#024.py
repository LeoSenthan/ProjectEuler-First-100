from itertools import permutations
perms=permutations([0,1,2,3,4,5,6,7,8,9])
n=0
for i in perms:
    n+=1
    if n==1000000:
        print(i)