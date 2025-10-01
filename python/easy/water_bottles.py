# 1518. Water Bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_drink = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            refills = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
            max_drink += refills
            empty_bottles += refills
        
        return max_drink