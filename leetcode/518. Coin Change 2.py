class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ## second attempt
        dp = [0] * (amount+1) # dp[i] is number of ways to build i

        for c in coins:
            for i in range(1, amount+1):
                if i < c:
                    continue
                elif i == c:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-c]

        return dp[-1]



        # ## first attempt
        # # dp[i] number of possible changes for amount i
        # dp = [0] * (amount+1)
        #
        # # this is critical, we go through coins in other loop to avoid duplicates.
        # for c in coins:
        #     for i in range(1, amount+1):
        #         if i < c:
        #             continue
        #         elif c == i:
        #             dp[i] += 1
        #         else:
        #             dp[i] += dp[i-c]
        #
        # return dp[-1]


print Solution().change(amount=1, coins=[1, 2, 5])  # 1
print Solution().change(amount=2, coins=[1, 2, 5])  # 2
print Solution().change(amount=3, coins=[1, 2, 5])  # 2
print Solution().change(amount=4, coins=[1, 2, 5])  # 3
print Solution().change(amount=5, coins=[1, 2, 5])  # 4
