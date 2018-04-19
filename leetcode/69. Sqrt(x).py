class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        if x == 1:
            return 1

        x0 = 1.0
        x_l = -1.0
        while abs(x_l-x0) >= 1:
            x_l = x0
            x0 = (x0+x/x0)/2

        return int(x0)


print Solution().mySqrt(4)
print Solution().mySqrt(8)