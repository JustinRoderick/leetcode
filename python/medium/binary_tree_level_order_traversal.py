# 102. Binary Tree Level Order Traversal

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if not root:
            return ans
        q.append(root)

        while q:
            sol = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                sol.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            ans.append(sol)
            
        return ans

# Notes
# Only add to queue if node is not null
# For loop to get all nodes at that current level and add to queue at once