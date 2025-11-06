# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            
            sol[num] = -1 if not stack else stack[-1]
            stack.append(num)
        
        return [sol[num] for num in nums1]
            
        