class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        a1 = None
        a2 = None

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:  # 1, 2
                if a1 is None:
                    a1 = nums[i-1]
                    a2 = nums[i]
                else:
                    if a1 < nums[i-1] or a2 < nums[i]:
                        return True # a1, nums[i-1], nums[i] or a1, a2, nums[i]
                    else:
                        a1 = nums[i-1]
                        a2 = nums[i]
            else:  # decreasing 5, 4
                if a1 is not None:
                    if a1 < nums[i] < a2:
                            a2 = nums[i]
                    if nums[i] > a2:
                        return True # a1, a2, nums[i]

        return False

# print Solution().increasingTriplet([1,2,3,4,5])
# print Solution().increasingTriplet([5,4,3,2,1])
# print Solution().increasingTriplet([5, 4, 3, 2, 1, 2, 1, 3])
# print Solution().increasingTriplet([2, 4, -2, -3])
# print Solution().increasingTriplet([0,4,2,1,0,-1,-3])
print Solution().increasingTriplet([1,2,-10,-8,-7])