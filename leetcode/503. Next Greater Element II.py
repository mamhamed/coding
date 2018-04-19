class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        if len(nums) == 1:
            return [-1]

        ans = [-1] * len(nums)
        n = len(nums)

        st = []
        for j in xrange(len(nums+nums)):
            i = j % n
            while len(st) > 0 and nums[st[-1]] < nums[i]:
                ans[st.pop()] = nums[i]
            st.append(i)

        return ans

print Solution().nextGreaterElements([1,2,3,2,1])