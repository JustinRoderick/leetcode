# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [{} for _ in range (9)]
        col_map = [{} for _ in range (9)]
        box_map = [{} for _ in range (9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                index = (row // 3) * 3 + (col // 3)
                if (val in row_map[row]) or (val in col_map[col]) or (val in box_map[index]):
                    return False
                row_map[row][val] = 1
                col_map[col][val] = 1
                box_map[index][val] = 1
                
        
        return True