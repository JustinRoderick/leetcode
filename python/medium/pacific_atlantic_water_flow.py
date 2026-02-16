# 417. Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        row = len(heights)
        col = len(heights[0])
        atlantic_visited = [[0 for _ in range(col)] for _ in range(row)]
        pacific_visited = [[0 for _ in range(col)] for _ in range(row)] 

        # pacific = 0, atlantic = 1
        def dfs(x: int, y: int, ocean: int):
            if ocean == 0:
                if pacific_visited[x][y] == 1:
                    return
                else:
                    pacific_visited[x][y] = 1
            else:
                if atlantic_visited[x][y] == 1:
                    return
                else:
                    atlantic_visited[x][y] = 1
            
            val = heights[x][y]
            if x > 0 and heights[x-1][y] >= val:
                dfs(x-1, y, ocean)
            if x < row-1 and heights[x+1][y] >= val:
                dfs(x+1, y, ocean)
            if y > 0 and heights[x][y-1] >= val:
                dfs(x, y-1, ocean)
            if y < col-1 and heights[x][y+1] >= val:
                dfs(x, y+1, ocean)


        for i in range(row):
            dfs(i, 0, 0)
            dfs(i, col-1, 1)
        for i in range(col):
            dfs(0, i, 0)
            dfs(row-1, i, 1)
        
        for i in range(row):
            for j in range(col):
                if pacific_visited[i][j] == 1 and atlantic_visited[i][j] == 1:
                    result.append([i, j])

        return result