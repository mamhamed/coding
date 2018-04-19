class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        A = [[1, 1] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    A[i][0] = max(A[j][0] + 1, A[i][0])

            count = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if A[i][0] == A[j][0] + 1:
                        count += A[j][1]
            A[i][1] = max(count, 1)

        print A
        a = max(A, key=lambda x: x[0])[0]
        return sum([x[1] for x in A if x[0] == a])


print Solution().findNumberOfLIS([1,3,5,4,7])
print Solution().findNumberOfLIS([2, 2, 2, 2, 2])
print Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3])