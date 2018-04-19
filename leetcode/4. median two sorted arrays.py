import bisect

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)+len(nums2)
        m = self.findKth(nums1, nums2, (n >> 1)+1)
        if n % 2 == 1:
            return m
        else:
            return (m + self.findKth(nums1, nums2, (n >> 1) ))/2.0

    def findKth(self, nums1, nums2, k):
        if not nums1: return nums2[k-1]
        if not nums2: return nums1[k-1]
        if k <= 1:
            return min(nums1[0], nums2[0])

        ind1, ind2 = min(len(nums1), k/2)-1, min(len(nums2), k/2)-1   # compare k/2th element
        m1, m2 = nums1[ind1], nums2[ind2]

        if m1 < m2:
            return self.findKth(nums1[ind1+1:], nums2, k-ind1-1)
        else:
            return self.findKth(nums1, nums2[ind2+1:], k-ind2-1)







# print Solution().findMedianSortedArrays([1,3], [2])  # 2
print Solution().findMedianSortedArrays([1,2], [3,4])  # 2
print Solution().findMedianSortedArrays([1,2], [1,2,3])  # 2
print Solution().findMedianSortedArrays([2], [3, 4])  # 3
print Solution().findMedianSortedArrays([1, 10], [3, 4, 5])  # 4
print Solution().findMedianSortedArrays([1, 2, 10], [3, 4])  # 3
print Solution().findMedianSortedArrays([1, 2, 10], [4])  # 2.5


print Solution().findKth([1, 2, 10], [4], 1)  # 3
print Solution().findKth([4], [1, 2, 10], 3)