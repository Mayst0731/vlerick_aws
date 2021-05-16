def countBattleships(board):
    def is_valid(row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        else:
            return True

    def dfs(row, col):
        if not is_valid(row, col):
            return
        if board[row][col] == ".":
            return

        board[row][col] = "."
        dfs(row + 1, col)   # below
        dfs(row - 1, col)   # above
        dfs(row, col + 1)   # right
        dfs(row, col - 1)   # left

    if not board:
        return

    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                count += 1
                dfs(row, col)

    return count


print(countBattleships([["X",".",".","X"],
                        [".",".",".","X"],
                        [".",".",".","X"]]))