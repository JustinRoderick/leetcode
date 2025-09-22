# 198. House Robber

# First Solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        max_profit = []
        max_profit.append(nums[0])
        if nums[1] > nums[0]:
            max_profit.append(nums[1])
        else:
            max_profit.append(nums[0])
        
        for i in range(2, n):
            max_profit.append(max((nums[i] + max_profit[i-2]), max_profit[i-1]))

        return max(max_profit[n-1], max_profit[n-2])

# Second Solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])

        for i in range(2, n):
            cur = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, cur
        
        return cur