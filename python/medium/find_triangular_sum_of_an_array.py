# 2221. Find Triangular Sum of an Array

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for i in range(n-1):
            for j in range(n-1):
                nums[j] = (nums[j] + nums[j + 1]) % 10
            n -= 1
        
        return nums[0]