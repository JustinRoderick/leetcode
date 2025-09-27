# 812. Largest Triangle Area

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0

        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j + 1, n):
                    x3, y3 = points[k][0], points[k][1]
                    cur_area = float(0.5) * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))
                    if cur_area > max_area:
                        max_area = cur_area

        return max_area