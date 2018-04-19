class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        self.mem = [[-1]*n for _ in range(n)]
        a = self.helper(nums, 0, len(nums)-1)
        return a >= 0

    def helper(self, nums, start, end):
        if self.mem[start][end] != -1:
            return self.mem[start][end]

        if start == end:
            return nums[end]

        left = self.helper(nums, start+1, end)
        right = self.helper(nums, start, end-1)

        self.mem[start][end] = max(nums[start]-left, nums[end]-right)
        return self.mem[start][end]

print Solution().PredictTheWinner([1, 5, 233, 7])
print Solution().PredictTheWinner([1, 5, 2])
print Solution().PredictTheWinner([0])
print Solution().PredictTheWinner([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print Solution().PredictTheWinner([0,0,7,6,5,6,1])
