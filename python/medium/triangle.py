# 120. Triangle

# Solution one
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        min_sol = []
        for i in range(1, h+1):
            min_sol.append([float('inf')] * i)
        min_sol[0][0] = triangle[0][0]
        
        length = 1
        for i in range(1, h):
            for j in range(length + 1):
                if j == 0:
                    min_sol[i][j] = min_sol[i-1][j] + triangle[i][j]
                elif j == length:
                    min_sol[i][j] = min_sol[i-1][j-1] + triangle[i][j]
                else:
                    min_sol[i][j] = min(min_sol[i-1][j-1], min_sol[i-1][j]) + triangle[i][j]

            length += 1
        
        return min(min_sol[h-1])

# Solution two
# o(n) space

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, - 1, - 1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]) 

        return triangle[0][0]