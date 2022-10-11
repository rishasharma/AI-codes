chess = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]


def solve(chess,col):
    pos = check_sum(chess)
    if pos==8:
        return True
    
    for row in range (0,8):
        if valid(chess,row,col):
            chess[row][col]=1
            if solve(chess, col+1):
                return True
            chess[row][col] = 0
        else:
            chess[row][col]=0

    return False


def valid(chess, row, col):
    for i in range(col):
        if chess[row][i] == 1:
            return False
  
        
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if chess[i][j] == 1:
            return False
  
    for i, j in zip(range(row, 8, 1), 
                    range(col, -1, -1)):
        if chess[i][j] == 1:
            return False
  
    return True
  

def print_board(chess):
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            if chess[i][j]==1:
                chess[i][j]='Q'
            else:
                chess[i][j]='X'
            
            if j == 7:
                print(chess[i][j])
            else:
                print(str(chess[i][j]) + " ", end="")


def check_sum(chess):
    sum=0
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            if chess[i][j] == 1:
                    sum+=1
    return (sum)

    return None

solve(chess,0)
print_board(chess)
