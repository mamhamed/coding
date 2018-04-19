class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        unique_paths = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i >= 1 and j >= 1:
                    unique_paths[i][j] = unique_paths[i-1][j] + unique_paths[i][j-1]
                if i == 0 and j >= 1:
                    unique_paths[i][j] = unique_paths[i][j-1]
                if i >=1 and j == 0:
                    unique_paths[i][j] = unique_paths[i-1][j]

                if i==0 and j==0:
                    unique_paths[i][j] = 1

        return unique_paths[n-1][m-1]





print Solution().uniquePaths(3,2)