# 3541. Find Most Frequent Vowel and Consonant

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_set = set("aeiou")
        vowel = Counter()
        consonant = Counter()

        for char in s:
            if char in vowel_set:
                vowel[char] += 1
            else:
                consonant[char] += 1

        return (max(vowel.values(), default = 0) + max(consonant.values(), default = 0))