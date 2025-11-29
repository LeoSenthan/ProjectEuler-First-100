import numpy as np

# Constants
Size = 15

# Matrix from the problem statement
matrix = np.array([
    [7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
    [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
    [ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]
], dtype=np.uint16)

# Sum of the highest value of the current row and all further rows (sum[current..15])
max_remaining = np.zeros(Size, dtype=np.uint32)

def search(row=0, column_mask=0, current_sum=0, best_solution=0):
    # Done?
    if row == Size:
        return current_sum

    # Even if choosing the highest value of each of the next rows:
    # Is it possible that this combination exceeds the previously highest sum?
    if current_sum + max_remaining[row] <= best_solution:
        return 0

    # Look at all values of the current row
    for column in range(Size):
        # Column already used?
        mask = 1 << column
        if column_mask & mask != 0:
            continue

        # "Occupy" column and continue with next row
        current = search(row + 1, column_mask | mask, current_sum + matrix[row, column], best_solution)
        if best_solution < current:
            best_solution = current

    return best_solution

def main():
    # Find highest element of each row
    max_value_per_row = np.amax(matrix, axis=1)

    # Compute the maximum sum of the last rows, ignoring collisions (invalid choices)
    max_remaining[Size - 1] = max_value_per_row[Size - 1]
    for row in range(Size - 1, 0, -1):
        max_remaining[row - 1] = max_remaining[row] + max_value_per_row[row - 1]

    # Let's go!
    result = search()
    print(result)

if __name__ == "__main__":
    main()
