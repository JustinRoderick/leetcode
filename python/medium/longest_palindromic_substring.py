# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = [0, 0]
        
        def execute(l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l+1
                if length > (longest_palindrome[1] - longest_palindrome[0] + 1):
                    longest_palindrome[1] = r
                    longest_palindrome[0] = l
                l -= 1
                r += 1

        for i in range(len(s)):
            execute(i, i)
            execute(i, i+1)
        
        return s[longest_palindrome[0] : (longest_palindrome[1] + 1 )]