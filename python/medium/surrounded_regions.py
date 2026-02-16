# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def dfs(x: int, y: int):
            if board[x][y] != "O":
                return
            board[x][y] = "S"
            if x > 0 and board[x-1][y] == "O":
                dfs(x-1, y)
            if x < row - 1 and board[x+1][y] == "O":
                dfs(x+1, y)
            if y > 0 and board[x][y-1] == "O":
                dfs(x, y-1)
            if y < col - 1 and board[x][y+1] == "O":
                dfs(x, y+1)
        
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        for i in range(col):
            dfs(0, i)
            dfs(row-1, i)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"