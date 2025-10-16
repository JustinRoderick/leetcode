# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        ly = 0
        ry = n - 1
        row_index = 0
        lx = 0
        rx = m - 1
        while ly <= ry:
            mid = (ly + ry) // 2 
            if matrix[mid][0] <= target:
                row_index = mid
                ly = mid + 1
            else:
                ry = mid - 1
        while lx <= rx:
            mid = (lx + rx) // 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                lx = mid + 1
            else:
                rx = mid - 1
        
        return False