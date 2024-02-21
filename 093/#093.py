#4 unique numbers between 1-9
#Combinations is 9C4=126
#Permutations of different operators+-*/ is 4P3 = 24
for n1 in range(1,9):
    for n2 in range(1,9):
        if n1==n2:
            break
        for n3 in range(1,9):
            if n3==n2 or n3==n1:
                break
            for n4 in range(1,9):
                if n4==n3 or n4==n2 or n4==n1:
                    break