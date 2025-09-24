# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        prev = None
        for i in range(n-2):
            l = i + 1
            r = n - 1
            cur = nums[i]
            if cur > 0:
                break

            if cur == prev:
                continue

            while l < r:
                total = cur + nums[l] + nums[r]
                if total == 0:
                    if ans and ans[-1] == [cur, nums[l], nums[r]]:
                        l += 1
                        r -= 1
                        continue
                    
                    ans.append([cur, nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

            prev = cur
        
        return ans