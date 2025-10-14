# 2273. Find Resultant Array After Removing Anagrams

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        if n == 1:
            return words
        for i in range(n-1, 0, -1):
            if "".join(sorted(words[i])) == "".join(sorted(words[i-1])):
                del words[i]

        return words