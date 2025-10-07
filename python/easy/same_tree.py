# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and not q):
                return True
            elif((not p and q) or (p and not q)):
                return False
            else:
                return p.val == q.val and dfs(q.left, p.left) and dfs(q.right, p.right)
        
        return dfs(p, q)