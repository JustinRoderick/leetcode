# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ones = 0
        flipped_zero = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                flipped_zero += 1
            
            while flipped_zero > k:
                if nums[l] == 0:
                    flipped_zero -= 1
                l += 1
            
            if (r - l + 1) > max_ones:
                max_ones = r - l + 1

        return max_ones