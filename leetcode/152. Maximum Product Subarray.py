class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)

        for i in range(n):
            dp_max[i] = max(dp_max[i-1]*nums[i], nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(dp_min[i-1]*nums[i], nums[i], dp_max[i-1]*nums[i])

        return max(dp_max)


print Solution().maxProduct([3, -1, 4])
print Solution().maxProduct([2,3,-2,4])
print Solution().maxProduct([2,3,-2,4,-1])