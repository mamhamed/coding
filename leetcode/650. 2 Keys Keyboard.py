import numpy as np
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n == 3:
            return 3

        # # DFS approach
        # for i in range(n/2, 0,-1):
        #     if n % i == 0:
        #         return n/i + self.minSteps(i)
        #
        # return n

        # DP approach
        dp = [i for i in range(n+1)] # dp[i] is min number of operation to get i

        for i in range(2, n+1):
            for k in range(2, i/2):
                if i % k == 0:
                    dp[i] = min(dp[i], dp[k]+i/k)

        return dp[-1]




print Solution().minSteps(3)  # 3
print Solution().minSteps(4)  # 4
print Solution().minSteps(16)  # 8
print Solution().minSteps(12)  # 7