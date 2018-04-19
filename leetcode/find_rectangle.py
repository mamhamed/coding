class Solution():
    def find_rectangle(self, points):

        points = set(points)

        res = []
        for point1 in points:
            for point2 in points:
                if abs(point1[0]-point2[0]) > 0 and abs(point1[1]-point2[1]) > 0:
                    point3 = (point1[0], point2[1])
                    point4 = (point2[0], point1[1])

                    if point3 in points and point4 in points:
                        res.append((point1, point2))
        return res

points = [(1,2), (1,4), (5,2), (5,4), (1,0), (8,7), (5,3), (1,3), (6,2)]
print Solution().find_rectangle(points)

"""
dic_x
1 -> {2,4,3}

dic_y
2 -> {5,6}
4 -> {5}
"""