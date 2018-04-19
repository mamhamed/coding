import numpy as np
import sys

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        extended_nums = [1] + nums + [1]
        n = len(extended_nums)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] to denote maximum gain from balloon range i to j

        # this is dp solution, the dfs solution gives tle
        # if there was only two balloon the last one times the boundary + last one gives the best value
        #
        # first get the array from 0 to i
        # then come back from backward
        # k is between j and i and is the last ball to burst
        for i in range(1, n-1):  # assuming the array is nums[:i]
            for j in range(i, 0, -1):
                for k in range(j, i+1): # k is the last ball to burst between j and i
                    dp[j][i] = max(dp[j][i], dp[j][k-1] + dp[k+1][i] +
                                   # below is the gain you get by bursting the last balloon from and l and r as boundary
                                   extended_nums[i+1]*extended_nums[k]*extended_nums[j-1]
                                   )

        return dp[1][-2]

    #     # this is dfs solution which give TLE
    #     self.memo = {}
    #     return self.dfs(nums)
    #
    # def dfs(self, nums):
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #
    #     if n == 1:
    #         return nums[0]
    #
    #     if n == 2:
    #         return nums[0]*nums[1]+max(nums[0], nums[1])
    #
    #     key = self.make_key(nums)
    #     if key in self.memo:
    #         return self.memo[key]
    #
    #     res = 0
    #     for i in range(n):
    #         if i == 0:
    #             res = max(res, nums[i]*nums[i+1]+self.dfs(nums[1:]))
    #         elif i == n-1:
    #             res = max(res, nums[i]*nums[i-1]+self.dfs(nums[:n-1]))
    #         else:
    #             res = max(res, nums[i-1]*nums[i]*nums[i+1]+self.dfs(nums[:i]+nums[i+1:]))
    #
    #     self.memo[key] = res
    #     return self.memo[key]
    #
    # def make_key(self, nums):
    #     return str(nums)


print Solution().maxCoins([3,1,5,8])
print Solution().maxCoins([9,76,64,21,97,60])
print Solution().maxCoins([2,4,8,4,0,7,8,9,1,2,4,7,1,7,3,6])



