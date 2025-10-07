# 101. Symmetric Tree

# DFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if(not p and not q):
                return True
            if((not p and q) or (p and not q) or (p.val != q.val)):
                return False
            
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        
        return dfs(root.left, root.right)