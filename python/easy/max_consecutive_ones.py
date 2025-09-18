# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max_ones:
                    max_ones = count
            else:
                count = 0
        
        return max_ones