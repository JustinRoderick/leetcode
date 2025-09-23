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

