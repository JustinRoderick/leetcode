# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = {}
        char = list(s)
        n = len(char)
        max_length = 0
        l = 0
        for r in range(n):
            if char[r] not in cur:
                cur[char[r]] = None

            else:
                key_list = list(cur.keys())
                for key in key_list:
                    del cur[key]
                    l += 1
                    if key == char[r]:
                        break
                cur[char[r]] = None
        
            if (r - l + 1) > max_length:
                max_length = r - l + 1
        
        return max_length