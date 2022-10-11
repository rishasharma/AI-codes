#knight's tour
chess=[[-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1]]


pos=1
xm = [2, 1, -1, -2, -2, -1, 1, 2]
ym = [1, 2, 2, 1, -1, -2, -2, -1]
    

def solve(board, curx, cury, xm, ym, pos):
    if(pos == 64):
        return True
    
    for i in range(8):
        xpos = curx + xm[i]
        ypos = cury + ym[i]
        if (valid (xpos, ypos, board)):
            board[xpos][ypos] = pos
            if(solve(board, xpos, ypos, xm, ym, pos+1)):
                return True
            board[xpos][ypos] = -1
    return False


def valid(x,y,board):
    if (x >= 0 and y >= 0 and x < 8 and y < 8 and board[x][y] == -1):
        return True
    return False

def print_board(chess):
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            if j == 7:
                print(chess[i][j])
            else:
                print(str(chess[i][j]) + " ", end="")

solve(chess, 0, 0, xm, ym, pos)
print_board(chess)
