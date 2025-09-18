# 3136. Valid Word

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set("aeiou")

        has_vowel = False
        has_consonant = False

        word = word.lower()
        if len(word) < 3:
            return False
        
        for char in word:
            if not (char.isalpha() or char.isdigit()):
                return False

            if char in vowels:
                has_vowel = True

            elif char.isalpha():
                has_consonant = True
        
        return has_vowel and has_consonant
            
            

