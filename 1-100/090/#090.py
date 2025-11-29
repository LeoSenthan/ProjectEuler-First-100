from itertools import combinations

squares = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
cubes = list(combinations([0,1,2,3,4,5,6,7,8,6], 6))

def valid(cube1, cube2):
    return all(x in cube1 and y in cube2 or x in cube2 and y in cube1 for x, y in squares)

count=0
for i, c1 in enumerate(cubes):
    for c2 in cubes[:i]:
        if valid(c1, c2):
            count += 1
print(count)
