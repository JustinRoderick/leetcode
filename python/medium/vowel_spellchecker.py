# 966. Vowel Spellchecker

class Solution:
    def devowel(self, word: str) -> str:
        vowels = set("aeiou")
        return "".join("#" if char in vowels else char for char in word)
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_list = set(wordlist)
        output = []

        lowercase_map = {}
        devowel_map = {}

        for word in wordlist:
            lowercase_word = word.lower()
            devowel_word = self.devowel(lowercase_word)
    
            if lowercase_word not in lowercase_map:
                lowercase_map[lowercase_word] = word
            if devowel_word not in devowel_map:
                devowel_map[devowel_word] = word

        for i in range(len(queries)):
            lowercase_query = queries[i].lower()
            devowel_query = self.devowel(lowercase_query)
            
            if queries[i] in word_list:
                output.append(queries[i])

            elif lowercase_query in lowercase_map:
                output.append(lowercase_map[lowercase_query])

            elif devowel_query in devowel_map:
                output.append(devowel_map[devowel_query])
            
            else:
                output.append("")

        return output