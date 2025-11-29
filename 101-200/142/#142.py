from collections import defaultdict

h = defaultdict(list)
m = {}

for i in range(3, 1000000):
    for j in range(1, i // 2 + 1):
        y = 2 * (i * j - j ** 2)
        x = i ** 2 - y
        if y == x:
            continue
        m[(x, y)] = m.get((x, y), 0) + 1
        h[x].append(y)

        for k in range(len(h[x]) - 1):
            z = h[x][k]
            if (y, z) in m:
                print("Total:", x + y + z, "[", x, y, z, "]")
                exit()
