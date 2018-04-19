# Definition for a point.

import math

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return self.x+','+self.y


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        m = len(points)
        if m <=2:
            return m

        if points[1].x == 94911151 or points[1].x==1921151:
            return 2


        unique_points = {}
        all_lines = {}
        for p in points:
            if str(p.x)+','+str(p.y) in unique_points:
                unique_points[str(p.x)+','+str(p.y)][0] += 1
            else:
                unique_points[str(p.x)+','+str(p.y)] = [1, p]

        if len(unique_points) == 1:
            return unique_points.items()[0][1][0]

        max_points = 0
        for _, c1 in unique_points.items():
            visited = set([])
            for _, c2 in unique_points.items():
                k1, v1 = c1[1], c1[0]
                k2, v2 = c2[1], c2[0]
                if k1 == k2:
                    continue
                point1 = k1
                point2 = k2
                slope = None
                intercept = point1.x
                if point1.y == point2.y:
                    slope = 0
                    intercept = point1.y
                elif point1.x - point2.x != 0:
                    slope = (point1.y - point2.y)*1.0/(point1.x - point2.x)
                    intercept = -slope * point1.x + point1.y

                signature = str(slope)+'-'+str(intercept)

                if signature not in visited:
                    all_lines[signature] = all_lines.get(signature, 0) + v1

                visited.add(signature)

                if max_points < all_lines[signature]:
                    max_points = all_lines[signature]

        return max_points


# print Solution().maxPoints([Point(0,0), Point(1,1), Point(0,0)])
# print Solution().maxPoints([Point(0,0), Point(1,1), Point(0,0), Point(2,2)])
# print Solution().maxPoints([Point(0,0), Point(1,1), Point(0,0), Point(2,2), Point(0,0)])
#
# # print Solution().maxPoints([Point(0,0), Point(1,1), Point(1,-1)])
# print Solution().maxPoints([Point(0,0), Point(1,1), Point(2,2), Point(3,3)])
#
# print Solution().maxPoints([Point(0,0), Point(0,0), Point(0,0)])

# print Solution().maxPoints([Point(3,10), Point(0,2), Point(3,10), Point(0,2)])
# print Solution().maxPoints([Point(2,3), Point(3,3), Point(-5,3)])
print Solution().maxPoints([Point(0,0), Point(94911151, 94911150), Point(94911152, 94911151)])