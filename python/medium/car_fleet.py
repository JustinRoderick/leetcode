# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        if n == 1:
            return 1
        
        stack = []
        pairs = []
        for i in range(n):
            pairs.append((position[i], speed[i]))
        pairs = sorted(pairs, reverse=True)

        for i in range(n):
            time = (target - pairs[i][0]) / pairs[i][1]
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
            
        return len(stack)