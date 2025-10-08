# 200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i:int, j:int):
            if grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                if i != m-1: dfs(i+1, j)
                if i != 0: dfs(i-1, j)
                if j != n-1: dfs(i, j+1)
                if j != 0: dfs(i, j-1)

                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count