class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        profit_at_i = [0] * len(prices)
        for i in xrange(len(prices)):
            if i == 0:
                profit_at_i[i] = 0
            else:
                profit_at_i[i] = max(prices[i] - prices[i-1] + profit_at_i[i-1], 0)

        return max(profit_at_i)





print Solution().maxProfit([])
print Solution().maxProfit([1])
print Solution().maxProfit([7, 1, 5, 3, 6, 4]) # 5
print Solution().maxProfit([7, 6, 4, 3, 1]) # 0
print Solution().maxProfit([7, 6, 4, 3, 1, 10]) # 9
print Solution().maxProfit([7, 6, 4, 3, 9, 10])