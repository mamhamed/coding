class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        if n == 1:
            return 1

        mat = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    mat[i] = max(mat[i], mat[j]+1)

        max_len = max(mat)
        print max_len
        # if max is 1 each number has
        if max_len == 1:
            return len(nums)

        num_paths = [0] * n
        mat = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if mat[j]+1 == max_len:
                        if num_paths[i] == 0:
                            num_paths[i] = num_paths[j]
                        num_paths[i] += num_paths[j]
                    mat[i] = max(mat[i], mat[j]+1)

        return num_paths

# print Solution().findNumberOfLIS([1,3,5,4,7])
# print Solution().findNumberOfLIS([2,2,2])
#
# print Solution().findNumberOfLIS([11, 12, 9, 10, 7, 8])

print Solution().findNumberOfLIS([1,2,4,3,5,4,7,2])