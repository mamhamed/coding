class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums

        n = len(nums)
        mem = nums[0]
        j = 1
        for i in xrange(1, n):
            if nums[i] == mem:
                continue
            else:
                mem = nums[i]
                j += 1

        return j

print Solution().removeDuplicates([])
print Solution().removeDuplicates([1, 1, 2])