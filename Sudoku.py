sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(sudo):
    pos = check_0(sudo)
    if not pos:
        return True
    else:
        row, col = pos
        
    for i in range(1,10):
        if valid(sudo, i, row, col):
            sudo[row][col] = i

            if solve(sudo):
                return True
            sudo[row][col] = 0

    return False


def valid(sudo, num, row,col):
    for i in range(len(sudo[0])):
        if sudo[row][i] == num:
            return False

    for i in range(len(sudo)):
        if sudo[i][col] == num:
            return False

    x = col // 3
    y = row // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if sudo[i][j] == num:
                return False

    return True


def print_board(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if j == 8:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="")


def check_0(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                return (i, j)

    return None

solve(sudoku)
print_board(sudoku)
