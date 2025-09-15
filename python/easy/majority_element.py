# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curmax = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                curmax = nums[i]
                count = 1
            elif nums[i] == curmax:
                count += 1
            
            else: count -= 1

        return curmax