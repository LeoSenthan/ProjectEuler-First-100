limit = 1000 * 1000 * 1000
sum_value = 0

for i in range(limit):
    prod = 1
    tmp = 7
    while tmp <= limit:
        prod *= (i // tmp) % 7 + 1
        tmp *= 7
    sum_value += (i % 7 + 1) * prod

print(sum_value)
