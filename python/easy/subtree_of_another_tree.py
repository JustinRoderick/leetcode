# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree (root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if (not root and not subRoot):
                return True
            if ((not root and subRoot) or (root and not subRoot)):
                return False
            else:
                return root.val == subRoot.val and sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        def subTree (root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if root.val == subRoot.val and sameTree(root, subRoot):
                return True
            
            return subTree(root.left) or subTree(root.right)

        return subTree(root)