import numpy as np
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        m = len(dungeon[0])
        mat = np.zeros([n,m]) # best life of knight at i,j
        mat[n-1][m-1] = max(1, 1-dungeon[n-1][m-1])
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i < n-1 and j < m-1:
                    mat[i][j] = max(1, min(mat[i+1][j], mat[i][j+1]) - dungeon[i][j])
                elif i < n-1:
                    mat[i][j] = max(1, mat[i+1][j]-dungeon[i][j])
                elif j < m-1:
                    mat[i][j] = max(1, mat[i][j+1]-dungeon[i][j])

        return mat[0][0]


dungeon = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]
           ]
print Solution().calculateMinimumHP(dungeon)


print "--------------"
dungeon = [[-2, -3, -30],
           [-5, -10, 30],
           [10, 30, -5]
           ]
print Solution().calculateMinimumHP(dungeon)
