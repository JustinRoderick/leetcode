# 2749. Minimum Operations to Make the Integer Zero

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        iterations = 1
        while True:
            k = num1 - (iterations * num2)
            if k < iterations:
                return -1
            if k.bit_count() <= iterations:
                return iterations
            
            iterations += 1