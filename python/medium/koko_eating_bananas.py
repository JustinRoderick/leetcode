# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        high = max(piles)
        low = 1
        res = high
        
        while low <= high:
            mid = (high + low) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                res = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return res