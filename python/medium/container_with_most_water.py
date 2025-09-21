# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            
            dif = height[l] - height[r]

            if dif <= 0:
                l += 1
            else:
                r -= 1
        
        return max_area
