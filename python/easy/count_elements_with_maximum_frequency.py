# 3005. Count Elements With Maximum Frequency

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_value = max(counter.values())
        amount = 0
        for count in counter.values():
            if count == max_value:
                amount += count
        
        return amount