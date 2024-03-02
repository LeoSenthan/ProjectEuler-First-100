def find_eulercoins(x, m):
    min_eulercoin = x
    sum_eulercoins = min_eulercoin
    n = 1

    while True:
        n += 1
        current = (x * n) % m
        if current < min_eulercoin:
            min_eulercoin = current
            sum_eulercoins += min_eulercoin
            break

    # Calculate the period of the sequence
    period = n

    # Calculate how many times the sequence repeats fully
    full_repeats = m // period

    # Calculate the sum for fully repeated sequences
    sum_eulercoins += full_repeats * min_eulercoin * full_repeats

    # Handle the remaining part of the sequence
    remaining_length = m % period
    n = 1
    while n <= remaining_length:
        current = (x * n) % m
        if current < min_eulercoin:
            min_eulercoin = current
            sum_eulercoins += min_eulercoin
        n += 1

    return sum_eulercoins

x = 1504170715041707
m = 4503599627370517

sum_of_eulercoins = find_eulercoins(x, m)
print(sum_of_eulercoins)
