class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0

        high_to_left = range(n)
        high_to_right = range(n)
        high_to_right[n-1] = n
        high_to_left[0] = -1
        for i in range(1,n):
            p = i-1
            while p >= 0 and heights[p] >= heights[i] and p != high_to_left[p]:
                p = high_to_left[p]
            high_to_left[i] = p

        for i in range(n-1,-1,-1):
            p = i + 1
            while p <= n-1 and heights[p] >= heights[i] and p != high_to_right[p]:
                p = high_to_right[p]

            high_to_right[i] = p


        val = 0
        for i in range(n):
            val = max(val, (high_to_right[i]-high_to_left[i]-1)*heights[i])

        return val


print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([1,2,3,4,5])
print Solution().largestRectangleArea([5,4,3,2,1])
print Solution().largestRectangleArea([5])