import numpy as np

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1:
            return 1

        perfect_sqrt = [x for x in range(n+1)]
        for i in range(n+1):
            for j in range(int(np.floor(np.sqrt(i)))+1):
                if j*j == i:
                    perfect_sqrt[i] = 1
                else:
                    perfect_sqrt[i] = min(perfect_sqrt[i], perfect_sqrt[i-j*j]+perfect_sqrt[j*j])


        return perfect_sqrt[n]




print Solution().numSquares(5)
print Solution().numSquares(12)
print Solution().numSquares(13)
print Solution().numSquares(42)
print Solution().numSquares(105)
