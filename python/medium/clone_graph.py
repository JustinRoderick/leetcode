# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()
        visited = {}
        if not node:
            return None
        final = Node(node.val)
        visited[node.val] = final
        q.append([final, node])

        while q:
            cur_nodes = q.popleft()
            for neighbor in cur_nodes[1].neighbors:
                if neighbor.val in visited:
                    cur_nodes[0].neighbors.append(visited[neighbor.val])
                else:
                    new_node = Node(neighbor.val)
                    visited[neighbor.val] = new_node
                    cur_nodes[0].neighbors.append(new_node)
                    q.append([new_node, neighbor])
        
        return final