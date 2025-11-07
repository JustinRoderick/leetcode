# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answers = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            num = temperatures[i]
            while stack and stack[-1][1] <= num:
                stack.pop()
            if stack and stack[-1][1] > num:
                answers[i] = stack[-1][0] - i
            
            stack.append((i, num))

        return answers