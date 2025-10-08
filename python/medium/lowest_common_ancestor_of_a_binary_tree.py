# 236. Lowest Common Ancestor of a Binary Tree
# Notes
# If node is None return none so left and right could be None
# return left or right allows you to go further down the tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node: 'TreeNode') -> 'TreeNode':
            if not node:
                return None
            if (node == p or node == q):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            return left or right

        return dfs(root)

# Better solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        if (root == p or root == q):
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
            
        return left or right