# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur_node = root
        while cur_node != None:
            if cur_node.val == val:
                break
            elif cur_node.val < val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

        return cur_node