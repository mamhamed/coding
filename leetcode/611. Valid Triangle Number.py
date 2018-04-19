class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorted_nums = sorted(nums)

        res = 0
        for i in xrange(n-1, -1, -1):
            start, end = 0, i-1
            while start < end:
                if sorted_nums[start] + sorted_nums[end] > sorted_nums[i]:
                    res += end - start
                    end -= 1
                else:
                    start += 1

        return res


print Solution().triangleNumber([2,2,3,4])