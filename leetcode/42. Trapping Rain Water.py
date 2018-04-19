class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if height is None or len(height) <= 1:
            return 0

        start = 0
        while start+1 < len(height) and height[start+1] > height[start]:
            start += 1

        if start == len(height):
            return 0

        end = len(height) - 1
        while end > 0 and height[end-1] > height[end]:
            end -= 1

        if end == 0:
            return 0

        total = 0
        while start < end:
            left = height[start]
            right = height[end]
            if left <= right:
                while left >= height[start] and start < end:
                    total += left - height[start]
                    start += 1
            else:
                while right >= height[end] and start < end:
                    total += right - height[end]
                    end -= 1


        return total

print Solution().trap([1,2,3,4,5])
print Solution().trap([5,4,3,2,1,0])
print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print Solution().trap([5,2,1,2,1,5])
