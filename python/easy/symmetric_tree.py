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

# BFS
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q1 = deque()
        q2 = deque()
        q1.append(root.left)
        q2.append(root.right)

        while q1 and q2:
            curq1 = q1.popleft()
            curq2 = q2.popleft()

            if (not curq1 and not curq2):
                continue
            if((not curq1 or not curq2) or (curq1.val != curq2.val)):
                return False
            q1.append(curq1.left)
            q1.append(curq1.right)
            q2.append(curq2.right)
            q2.append(curq2.left)

        return True