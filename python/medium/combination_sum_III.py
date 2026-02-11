# 216. Combination Sum III

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sol = []
        # If the required amount is greater than the sum then it is impossible
        if k > n:
            return sol
        
        def backtrack(cur, index, target, k):
            # Solution
            if target == 0 and k == 0:
                sol.append(cur[:])
            # Iterate through all numbers
            for i in range(index, 10):
                if i > target or k < 0:
                    break
                cur.append(i)
                backtrack(cur, i+1, target-i, k-1)
                cur.pop()            
                
        backtrack([], 1, n, k)
        return sol