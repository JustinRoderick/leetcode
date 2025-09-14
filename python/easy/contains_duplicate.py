# 217. Contains Duplicate

# First slow solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap={}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            if nums[i] in numMap and numMap[nums[i]] != i:
                return True
        
        return False
    
# Little faster
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        max_count = max(count.values())
        
        if max_count >= 2: return True
        
        else: return False
