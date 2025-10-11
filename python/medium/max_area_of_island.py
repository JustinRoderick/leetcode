# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i:int, j:int) -> int:
            if grid[i][j] == 1:
                grid[i][j] = 0
                area = 1
                if(i > 0): area += dfs(i-1, j)
                if(i < n-1): area += dfs(i+1, j)
                if(j > 0): area += dfs(i, j-1)
                if(j < m-1): area += dfs(i, j+1)
                return area
            
            else:
                return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    if area > max_area:
                        max_area = area
        
        return max_area