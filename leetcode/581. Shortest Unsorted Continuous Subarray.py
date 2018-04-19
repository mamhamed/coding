class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        start, end = -1, -2
        min_val, max_val = nums[n-1], nums[0]
        for i in range(1, n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n-i-1])
            if nums[n-i-1] > min_val:
                start = n-i-1
            if nums[i] < max_val:
                end = i

        return end-start+1


# print Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
# print Solution().findUnsortedSubarray([1, 3, 2, 2, 2])
# print Solution().findUnsortedSubarray([1, 4, 3, 4, 4, 4])
# print Solution().findUnsortedSubarray([2, 3, 3, 2, 4])
print Solution().findUnsortedSubarray([1, 2, 3, 4])