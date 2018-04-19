class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0

        dp1 = [0] * n  # dp1[i] gain by first time selling stock at i
        hold = [0] * n
        dp2 = [0] * n  # dp2[i] gain by second time selling stock at i

        for i in range(1, n):
            dp1[i] = max(dp1[i-1]-prices[i-1]+prices[i], 0)

        for i in range(1, n):
            if i >= 2:
                dp2[i] = max(dp2[i-1]-prices[i-1]+prices[i],
                         hold[i-1], dp1[i])
            else:
                dp2[i] = dp1[i]

            hold[i] = max(hold[i-1], dp1[i])

        return max(dp2)

# print Solution().maxProfit([7, 6, 4, 3, 1, 10])
# print Solution().maxProfit([7, 6, 4, 3, 9, 10])
# print Solution().maxProfit([7, 1, 5, 3, 6, 4])
# print Solution().maxProfit([7, 1, 1, 3, 6, 4])

print Solution().maxProfit([3,2,6,5,0,3])