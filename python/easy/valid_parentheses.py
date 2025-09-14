# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in dict:
                stack.append(char)
            if char in dict:
                if (not stack) or (stack.pop() != dict[char]):
                    return False
        if stack:
            return False
        return True 