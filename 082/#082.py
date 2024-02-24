# Read the matrix from the file
#Reused Code from 81
matrix = [list(map(int, row.split(','))) for row in open("081/#081.txt").readlines()]
# Extract the value of each cell in the last column
finalvalue = [matrix[i][-1] for i in range(len(matrix))]
for column in range(len(matrix[0])-2, -1, -1):
    finalvalue[0]+=matrix[0][column]
    for row in range(1, len(matrix)):
        finalvalue[row] = min(finalvalue[row], finalvalue[row-1])+matrix[row][column]
    # Update the cost for rows in reverse order
    for row in range(len(matrix)-2, -1, -1):
        finalvalue[row] = min(finalvalue[row],finalvalue[row+1]+matrix[row][column])
print(min(finalvalue))