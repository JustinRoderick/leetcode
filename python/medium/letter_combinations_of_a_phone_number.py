# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map: dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        sol = []
        answer = []
        n = len(digits)
        
        def backtrack(answer: list, index: int):
            if index == n:
                string = ''.join(answer)
                sol.append(string)
                return

            for value in digit_map[digits[index]]:
                answer.append(value)
                backtrack(answer, index + 1)
                answer.pop()

        backtrack(answer, 0)
        return sol    