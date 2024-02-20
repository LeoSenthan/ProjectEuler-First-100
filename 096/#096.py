with open("096/#096.txt") as f:
    words=f.readlines()
def solve_sudoku(grid):
    # Convert grid to 2d list
    sudoku = [list(map(int, grid[i:i+9])) for i in range(0, 81, 9)]
    def is_valid(row, col, num):
        if num in sudoku[row]:
            return False
        if num in [sudoku[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if sudoku[start_row + i][start_col + j] == num:
                    return False
        return True
    def backtrack():
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    for num in range(1,10):
                        if is_valid(row, col, num):
                            sudoku[row][col] = num
                            if backtrack():
                                return True
                            sudoku[row][col] = 0
                    return False
        return True
    backtrack()
    # Convert back to grid
    solved_grid = ''.join(''.join(map(str, row)) for row in sudoku)
    return solved_grid
total=0
for i in range(0,50):
    grid = ""
    gridlines=words[i*10+1:i*10+10]
    for line in gridlines:
        grid+=line
    grid=grid.replace("\n","")
    solution = solve_sudoku(grid)
    print(solution)
    total+=int(solution[0:3])
print(total)