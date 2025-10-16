# 567. Permutation in String

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        count = Counter(s1)
        window = Counter(s2[:n])
        if count == window:
            return True
        
        for i in range(n, m):
            start = s2[i - n]
            end = s2[i]
            window[start] -= 1
            window[end] += 1
            if window[start] == 0:
                del window[start]
            if count == window:
                return True

        return False