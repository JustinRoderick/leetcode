# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and not q):
                return True
            elif((not p and q) or (p and not q)):
                return False
            else:
                return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)

# BFS
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            curq1 = q1.popleft()
            curq2 = q2.popleft()
            if(not curq1 and not curq2):
                continue
            if(not curq1 and curq2) or (curq1 and not curq2) or (curq1.val != curq2.val):
                return False

            q1.append(curq1.left)
            q1.append(curq1.right)
            q2.append(curq2.left)
            q2.append(curq2.right)

        return True 