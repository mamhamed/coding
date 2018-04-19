class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums) % 2 != 0:
            return False

        s = sum(nums)

        dp = [[False]*s for _ in range(len(nums))] # dp[i][j] if we can build sum j by numbers 0 till i-1
        dp[0][0] = True
        for i in range(len(nums)):
            for j in range(s):
                if j == nums[i]:
                    dp[i][j] = True
                elif j > nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]

        return dp[-1][s/2]

        """
        first practice
        """
        d = sum(nums)
        if d % 2 != 0:
            return False

        n = len(nums)
        # dp[i][j] is if we can build sum j with numbers 0 to i-1
        dp = [[False]*d for _ in range(n)]

        for i in range(n):
            for j in range(d):
                if j == 0:
                    dp[i][j] = True
                else:
                    residual = j-nums[i]
                    dp[i][j] = dp[i-1][j] or (dp[i-1][residual] and residual >=0 )

        print dp[-1][d/2]

    """
    dfs result in TLE
    """
    def dfs(self, nums, s):
        if s < 0:
            return False

        if len(nums) == 0:
            return True

        if len(nums) == 1:
            return nums[0] == s

        return self.dfs(nums[1:], s-nums[0]) or self.dfs(nums[1:], s)


print Solution().canPartition([1, 5, 11, 5])
print Solution().canPartition([1, 2, 3, 5])
print Solution().canPartition([2, 2, 3, 5])
print Solution().canPartition([1,5,11,5])