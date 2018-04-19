class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]

        dequeue = []
        res = []
        for i,v in enumerate(nums):
            while len(dequeue) > 0 and nums[dequeue[-1]] < v:
                dequeue.pop()
            while len(dequeue) > 0 and dequeue[0] <= i-k:
                dequeue.pop(0)

            dequeue.append(i)
            res.append(nums[dequeue[0]])

        return res[k-1:]


print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 1)
print Solution().maxSlidingWindow([1, -1], 1)
print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print Solution().maxSlidingWindow([7,6,5,4,3,2,1], 3)
print Solution().maxSlidingWindow([7,2,4], 2)