import time

start = time.time()
total = 0

n = 1
while n**2 < 10**16:  # 5-digit squares
    sq = n**2
    s = str(sq)
    for i in range(max(1,len(s)//2-1), min(len(s),len(s)//2+2)):
        left = int(s[:i]) if s[:i] != '' else 0
        right = int(s[i:])
        if s[i]=="0":
            continue  # Avoid division by zero or invalid Kaprekar
        if (left + right) ** 2 == sq:
            print(sq)
            total += sq
            break  # Avoid counting same number multiple times
    n += 1

print("Total:", total)
print("Time:", time.time() - start)
