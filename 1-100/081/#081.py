# Start top-left move down to right
# Replace each column with minimal sums
#map function is map(function,iterable) which results in each item in iterable having function applied to it
# Read the matrix from file
matrix = [list(map(int, row.split(','))) for row in open("081/#081.txt").readlines()]
# Traverse the matrix to calculate minimal path sum
for i in range(1, len(matrix)):  # columns
    for j in range(1, len(matrix[0])):  # rows
        # Update current cell with the minimal path sum
        matrix[i][0] += matrix[i - 1][0]  # Update column-wise
        matrix[0][j] += matrix[0][j - 1]  # Update row-wise
        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])  # Update diagonal-wise
print(matrix[-1][-1])

