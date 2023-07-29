import itertools

# field is 9x9
matrix = 9

# print the solution


def solution(grid):
    global matrix
    print("Solution is: ")
    for x in range(matrix):
        for y in range(matrix):
            print(grid[x][y], end=" ")
        print()

# function which solves each box


def check_valid_move(grid, row, col, num):
    # check if num num can be placed on the x axis
    for i in range(matrix):
        if grid[row][i] == num:
            return False

# check if num can be placed on the y axis
    for i in range(matrix):
        if grid[i][col] == num:
            return False

    # get current start and row column
    start_row_block = row - row % 3
    start_col_block = col - col % 3

# check if move is valid
    for x in range(3):
        for y in range(3):
            if grid[x + start_row_block][y + start_col_block] == num:
                return False
    return True


# check for possibility to place number

def solve_sudoku(grid, row, col):
    global matrix
    # check if we've solved the sudoku
    if row == matrix - 1 and col == matrix:
        return True

# we've reached the end of the columns, moving to the next row
    if col == matrix:
        row += 1
        col = 0

# check whether the square already has a value
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, matrix + 1):
        # if solving is possible, assign that sollution to the square
        if check_valid_move(grid, row, col, num):
            # assign number to the square
            grid[row][col] = num

            if solve_sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def create_grid() -> []:
    user_grid = []
    for i in range(matrix):
        user_input = input(f"Enter row #{i + 1}: ")
        row = [int(number) for number in user_input]
        user_grid.append(row)

    grid_length = len(list(itertools.chain(*user_grid)))

    if grid_length == 81:
        return user_grid
    else:
        raise Exception(f"Invalid grid amount. 81 indeed, got: {grid_length}")
