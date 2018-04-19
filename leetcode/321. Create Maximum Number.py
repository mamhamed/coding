import numpy as np
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        # the following works
        # I could not make it as dp
        arr = []
        for i in range(k+1):
            if i > len(nums1) or k-i > len(nums2):
                continue
            sub_nums1 = self.select(nums1, i)
            sub_nums2 = self.select(nums2, k-i)
            total = self.max_merge(sub_nums1, sub_nums2)
            if len(arr) == 0:
                arr = total
            elif arr < total:
                arr = total

        return arr

    def select(self, nums, k):
        n = len(nums)
        ret = []
        start = 0
        while k > 0:
            end = n - k + 1  # search end
            ind = np.argmax(nums[start: end])+start
            ret.append(ind)
            start = ind+1
            k -= 1
        return [nums[item] for item in ret]

    def max_merge(self, nums1, nums2):
        arr = []
        while nums1 or nums2:
            if nums1 > nums2:
                arr.append(nums1[0])
                nums1 = nums1[1:]
            else:
                arr.append(nums2[0])
                nums2 = nums2[1:]
        return arr


print Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)  # [9, 8, 6, 5, 3]
print Solution().maxNumber([6, 7], [6, 0, 4], 5)  # [6, 7, 6, 0, 4]
print Solution().maxNumber([3, 9], [8, 9], 3)  # [9, 8, 9]
print Solution().maxNumber([3, 6, 1, 9], [8, 9], 3)  # [9, 8, 9]
print Solution().maxNumber([1,2], [], 2)  # [9, 8, 9]