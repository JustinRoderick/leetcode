# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        good_position = n-1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= good_position:
                good_position = i

        
        return True if good_position == 0 else False 