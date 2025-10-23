# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def backtrack(cur: List[int], n: int):
            sol.append(cur[:])
            for i in range(n, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i+1)
                cur.pop()

        cur = []
        backtrack(cur, 0)
        return sol