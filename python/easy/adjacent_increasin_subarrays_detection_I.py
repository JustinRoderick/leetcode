# 3349. Adjacent Increasing Subarrays Detection I

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l1 = 0
        r1 = k - 1
        l2 = k
        r2 = l2 + k - 1

        while r2 < n:
            if (((nums[l1:l2] == sorted(nums[l1:l2])) and (len(set(nums[l1:l2])) == k)) and ((nums[l2:r2+1] == sorted(nums[l2:r2+1])) and (len(set(nums[l2:r2+1])) == k))):
                return True
            else:
                l1, r1, l2, r2 = l1+1, r1+1, l2+1, r2+1

        return False