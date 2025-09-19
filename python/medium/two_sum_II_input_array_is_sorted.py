# 167. Two Sum II - Input Array Is Sorted

# Second submission
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        if r == 1:
            return [1, 2]

        while l < r:
            num = numbers[l] + numbers[r]
            if num == target: return [l+1, r+1]

            elif num < target: l += 1

            else: r -= 1

# First submission
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        if n == 2:
            return [1, 2]

        cur = 0

        for num in numbers:
            l = cur + 1
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                num = numbers[mid] + numbers[cur]
                if target == num:
                    return [cur + 1, mid + 1]
                elif target > num:
                    l = mid + 1
                else:
                    r = mid - 1
                
            
            cur += 1