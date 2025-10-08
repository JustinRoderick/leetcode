# 2300. Successful Pairs of Spells and Potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        sol = [0] * n
        potions.sort()
        for i in range(n):
            min_potions = math.ceil(success / spells[i])
            l = 0
            r = m - 1
            while l <= r:
                mid = (r + l) // 2
                if potions[mid] >= min_potions:
                    sol[i] = m - mid
                    r = mid - 1
                else:
                    l = mid + 1
        
        return sol