# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        words = {}
        n = len(strs)
        for i in range(n):
            string = strs[i]
            char_arr = list(string)
            char_arr.sort()
            sorted_string = "".join(char_arr)
            if sorted_string in words:
                words[sorted_string].append(string)
            else:
                words[sorted_string] = [string]

        for value in words.values():
            sol.append(value)
        
        return sol