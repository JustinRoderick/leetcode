# 973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for i in range(len(points)):
            n = math.sqrt((0 - points[i][0])**2 + (0 - points[i][1])**2)
            points[i] = (n, [points[i][0], points[i][1]])
        
        heapq.heapify(points)

        return [heapq.heappop(points)[1] for _ in range(k)]