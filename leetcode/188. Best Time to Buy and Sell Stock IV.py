class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        if k == 0:
            return 0

        k = min(n, k)

        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        for i in xrange(1, n):
            dp1[i] = max(dp1[i-1]-prices[i-1]+prices[i], 0)

        if k == 1:
            return max(dp1)

        max_val = 0
        for j in xrange(1, k):
            for i in xrange(j, n):
                dp2[i] = max(dp2[i-1]-prices[i-1]+prices[i],
                           hold[i-1]-prices[i-1]+prices[i],
                           dp1[i],
                           0)
                hold[i] = max(hold[i-1], dp1[i-1])
                max_val = max(max_val, dp2[i])

                dp1[i-1] = dp2[i-1]
                hold[i-2] = 0

            dp1[-1] = dp2[-1]
            hold[-1] = 0
            hold[-2] = 0

        return max_val


    """
    # the following has mem problem
    dp1 = [[0]*k for _ in range(n)]
    dp2 = [[0]*k for _ in range(n)]
    hold = [[0]*k for _ in range(n)]
    for i in range(1, n):
            for j in range(k):
                if j == 0:
                    dp[i][j] = max(dp[i-1][j]-prices[i-1]+prices[i], 0)
                else:
                    if k > 1:
                        dp[i][j] = max(dp[i-1][j]-prices[i-1]+prices[i],
                                       hold[i-1][j-1]-prices[i-1]+prices[i],
                                       dp[i][j-1],
                                       0)

                        hold[i][j-1] = max(hold[i-1][j-1], dp[i-1][j-1])

        return max([x[-1] for x in dp])
    """


print Solution().maxProfit(2, [3,2,6,5,0,3])
print Solution().maxProfit(1, [3,2,6,5,0,3])
print Solution().maxProfit(1, [1,2])
print Solution().maxProfit(2, [2,1,2,0,1])
print Solution().maxProfit(2, [3,3,5,0,0,3,1,4])