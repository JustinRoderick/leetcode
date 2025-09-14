# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i
        
        for i in range(n):
            compliment = target - nums[i]
            if compliment in numMap and numMap[compliment] != i:
                return [numMap[compliment], i]

        return []