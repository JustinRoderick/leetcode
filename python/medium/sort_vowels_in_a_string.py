# 2785. Sort Vowels in a String

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        vowel_list = []

        for char in s:
            if char in vowels:
                vowel_list.append(char)
        
        sorted_vowel = sorted(vowel_list) 
        solution = []
        index = 0
        for i in range(len(s)):
            if s[i] in vowels:
                solution.append(sorted_vowel[index])
                index +=1
                continue
            
            solution.append(s[i])
            
        return ''.join(solution)