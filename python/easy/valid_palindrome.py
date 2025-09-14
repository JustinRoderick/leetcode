# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^A-Za-z0-9]', '', s)
        stack = []
        for char in s:
            stack.append(char)
        for char in s:
            if char != stack.pop():
                return False
        return True