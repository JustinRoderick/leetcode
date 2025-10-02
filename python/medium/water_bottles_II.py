# 3100. Water Bottles II

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        max_count = numBottles
        empty_bottles = numBottles
        full_bottles = 0

        while empty_bottles >= numExchange or full_bottles != 0:
            if empty_bottles >= numExchange:
                full_bottles += 1
                empty_bottles -= numExchange
                numExchange += 1

            else:
                empty_bottles += full_bottles
                max_count += full_bottles
                full_bottles = 0

        return max_count