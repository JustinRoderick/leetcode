# 153. Find Minimum in Rotated Sorted Array

# O(log n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            mid = (l + r) // 2
            if (mid != 0 and nums[mid-1] > nums[mid]):
                return nums[mid]
            elif (mid != n-1 and nums[mid+1] < nums[mid]):
                return nums[mid+1]
            elif nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return nums[0] if nums[0]<nums[n-1] else nums[n-1]
        

# O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
        