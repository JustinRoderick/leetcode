# 53. Maximum Subarray

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = [float("-inf")] * n

        max_sum[0] = nums[0]

        for i in range(1, n):
            max_sum[i] = max((max_sum[i-1] + nums[i]), nums[i])
        
        return max(max_sum)