# 215. Kth Largest Element in an Array

from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums) - k
        for num in nums:
            heappush(heap, num)
        for i in range(n):
            heappop(heap)
        
        return heappop(heap)