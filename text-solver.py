puzzle = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

# Function to print out the Sudoku Board
# Arguement:    2D list reperesenting puzzle
# Output:       No output, prints to console.
def print_board(board):
    # Print horizontal line every third row
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        # Print vertical line every third column
        for j in range(len(board)):
            if j%3 == 0 and j != 0:
                print("| ", end="")

            # Print space after element unless final element in row
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    # End function print_board()

# Search Sudoku Board for blank element, moves across row from right to left, top to bottom
# Arguement:    2D list reperesenting puzzle
# Output:      Returns coordinates of blank square, or False if none found
def find_blank(board):
    # Search row and column for blank element represented with a zero
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j) #(row, column)
    return False
    # End function find_blank()

# Checks if a number is valid for a given square
# Arguement:    2D list reperesenting puzzle, number to verify, square coordinates
# Output:       Returns True if number is a valid choice, else False
def valid(board, num, pos):
    # Check row
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3 # column postioning
    box_y = pos[0] // 3 # row positioning

    # iterate through relevant box only
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
    # End function valid()

def solve(board):
    find = find_blank(board)
    if not find:
        return True # Success if no blank squares found
    else:
        row, col = find

    for i in range(1,10): # Try numbers 1-9
        if valid(board, i , (row,col)):
            board[row][col] = i # Insert valid number

            if solve(board): # Recursively progress through all blanks
                return True
            # Provides backtracking condition
            board[row][col] = 0
        
    return False
# Print board, run solver, print result
print_board(puzzle)
solve(puzzle)
print("\n")
print_board(puzzle)