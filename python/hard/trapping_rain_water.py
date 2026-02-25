# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = 0
        max_right = 0
        total = 0
        while l <= r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            
            if max_left <= max_right:
                total += max(0, max_left - height[l])
                l += 1
            
            else:
                total += max(0, max_right - height[r])
                r -= 1

        return total