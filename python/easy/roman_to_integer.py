# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        n = len(s)

        for i in range(n):
            cur_val = numerals[s[i]]
            next_val = numerals[s[i+1]] if i < n-1 else 0
            if cur_val < next_val:
                num -= cur_val
            
            else:
                num += cur_val

        return num