# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        cur = []
        candidates.sort()

        def backtrack(i:int):
            if sum(cur) > target:
                return
            if sum(cur) == target:
                sol.append(cur[:])
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                    
                cur.append(candidates[j])
                backtrack(j+1)
                cur.pop()

        backtrack(0)
        return sol