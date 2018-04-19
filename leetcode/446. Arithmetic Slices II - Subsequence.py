class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # # using dp
        # if A is None or len(A) < 3:
        #     return 0
        # n = len(A)
        # # dp[i][j] is number of arithmetic slices end in i with dist i
        # total = 0
        # dp = [{} for _ in range(n)]
        # for i in range(len(A)):
        #     for j in range(i):
        #         k = A[i] - A[j]
        #         dp[i][k] = dp[i].get(k, 0) + 1
        #         if k in dp[j]:
        #             dp[i][k] += dp[j][k]
        #             total += dp[j][A[i]-A[j]]
        #
        # return total

        # using hashmap and math
        if A is None or len(A) < 3:
            return 0
        n = len(A)
        dic = {}
        for i in range(n):
            for j in range(i+1, n):
                diff = A[j] - A[i]
                dic[diff] = dic.get(diff, 0) + 1

        s = 0
        for k, v in dic.items():
            if v > 2:
                s += (v-2) * (v-1) / 2

        return s



print Solution().numberOfArithmeticSlices([2,4,6,8,10])  # 7
print Solution().numberOfArithmeticSlices([1,2,3])  # 1