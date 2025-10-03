# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index1 = m - 1
        index2 = n - 1
        insert = n + m - 1

        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[insert] = nums1[index1]
                index1 -= 1
            else:
                nums1[insert] = nums2[index2]
                index2 -= 1

            insert -= 1   