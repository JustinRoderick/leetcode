# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        ans = []
        n = len(candidates)

        def backtrack(i: int):
            if sum(sol) > target:
                return

            if sum(sol) == target:
                ans.append(sol[:])
                return
            
            for j in range(i, n):
                sol.append(candidates[j])
                backtrack(j)
                sol.pop()
            
        backtrack(0)
        return ans