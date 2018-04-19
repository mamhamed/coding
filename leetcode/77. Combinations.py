class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i+1 for i in range(n)]

        return self.create_combine(nums, k)


    def create_combine(self, nums, k):
        if len(nums) == 0 or len(nums) < k:
            return []

        if k == 0:
            return []

        if k == 1:
            return [[i] for i in nums]

        if len(nums) == k:
            return [nums]

        rest = nums[1:]
        comb_with_i = self.create_combine(rest, k-1)
        combine_with_i = [[nums[0]]+x for x in comb_with_i]
        comb_without_i = self.create_combine(rest, k)

        return combine_with_i + comb_without_i


print Solution().combine(4, 2)