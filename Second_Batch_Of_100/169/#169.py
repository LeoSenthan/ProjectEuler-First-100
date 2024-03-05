def numberofways(x):
    current = [x]
    count = 0
    while len(current) > 0:
        new = []
        for num in current:
            if num % 2 == 0:
                new.append(num / 2)
                new.append((num - 2) / 2)
            else:
                new.append((num - 1) / 2)
        count += new.count(1) + new.count(0)
        current = [n for n in new if n not in (0, 1)]
    return count
print(numberofways(10**25))
