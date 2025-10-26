# 994. Rotting Oranges

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            for _ in range(len(q)):                
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        q.append((nx,ny))
                        grid[nx][ny] = 2
            if q:
                minutes += 1
        
        for row in grid:
            for item in row:
                if item == 1:
                    return -1
        
        return minutes