# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_sequence = 0
        cur_sequence = 0
        for val in hashset:
            if (val - 1) not in hashset:
                cur_sequence = 1
                while val+1 in hashset:
                    cur_sequence += 1
                    val += 1
            

            if cur_sequence > longest_sequence:
                longest_sequence = cur_sequence

        return longest_sequence