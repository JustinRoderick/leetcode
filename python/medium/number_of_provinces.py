# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(x:int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            return parent[x]

        def union(x:int, y:int):
            parent1 = find(x)
            parent2 = find(y)

            if parent1 != parent2:
                parent[parent1] = parent2

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len({find(i) for i in range(n)})