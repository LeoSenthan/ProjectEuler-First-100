def count_laminae(max_tiles):
    count, a = 0, 1
    while True:
        b = 1
        while a ** 2 - b ** 2 <= max_tiles:
            count += 1
            b += 1
        if b > a:
            break
        a += 1
    return count

max_tiles = 100
print("HELLO")
result = count_laminae(max_tiles)
print("Number of different square laminae that can be formed with up to 1000000 tiles:", result)
