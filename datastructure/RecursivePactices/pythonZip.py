
def isValidSudoku(board) -> bool:

    return isValid_row(board) and isValid_col(board) and isValid_square(board)

def isValid_row(board):
    for row in board:
        if not isValid_lst(row):
            return False
    return True

def isValid_col(board):
    for col in zip(*board):
        if not isValid_lst(col):
            return False
    return True

def isValid_square(board):
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not isValid_lst(square):
                return False
    return True

def isValid_lst(lst):

    lst2 = [l for l in lst if l != '.']

    return len(set(lst2)) == len(lst2)


b = [[".",".",".",".",".",".","5",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     ["9","3",".",".","2",".","4",".","."],
     [".",".","7",".",".",".","3",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".","3","4",".",".",".","."],
     [".",".",".",".",".","3",".",".","."],
     [".",".",".",".",".","5","2",".","."]]

print(isValidSudoku(b))




