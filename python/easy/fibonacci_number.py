# 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        index1 = 0
        index2 = 1

        for _ in range(n-1):
            temp = index1 + index2
            index1 = index2
            index2 = temp
        
        return index2