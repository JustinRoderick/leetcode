# 347. Top K Frequent Elements

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = count.most_common()
        ans = []
        for i in range(k):
            ans.append(count[i][0])
        return ans

# Solution using heap

from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        for key, value in count.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)

        return [freq[1] for freq in heap]