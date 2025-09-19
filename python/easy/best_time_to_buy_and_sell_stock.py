# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        low = float('inf')

        for price in prices:
            if price <= low:
                low = price
            else:
                if max_profit < price - low:
                    max_profit = price - low
        
        return max_profit