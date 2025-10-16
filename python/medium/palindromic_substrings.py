# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and ((i-j <=2) or (dp[j+1][i-1] == True)):
                    dp[j][i] = True


        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    count += 1
        return count
