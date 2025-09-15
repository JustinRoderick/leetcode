# 1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        brokenLetters = set(brokenLetters)
        count = 0

        for word in words:
            if set(word) & brokenLetters:
                continue
            count += 1

        return count