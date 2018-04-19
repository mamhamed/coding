class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        sorted_nums = self.largestNumberArray(nums)
        num = ''.join([str(x) for x in sorted_nums])
        i = 0
        while i < len(num)-1 and num[i] == '0':
            i += 1
        return num[i:]

    def largestNumberArray(self, nums):
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums[0]]

        if n == 2:
            case1 = str(nums[0]) + str(nums[1])
            case2 = str(nums[1]) + str(nums[0])
            if case1 > case2:
                return nums
            else:
                return [nums[1], nums[0]]

        m = n/2
        nums1 = self.largestNumberArray(nums[:m])
        nums2 = self.largestNumberArray(nums[m:])

        i = j = 0
        sorted_nums = []
        while i < m and j < (n-m):
            i, j , a = self.compare_two(nums1, nums2, i, j)
            sorted_nums.append(a)

        while i < m:
            sorted_nums.append(nums1[i])
            i += 1

        while j < n-m:
            sorted_nums.append(nums2[j])
            j += 1

        return sorted_nums

    def compare_two(self, nums1, nums2, i, j):
        case1 = str(nums1[i])+str(nums2[j])
        case2 = str(nums2[j])+str(nums1[i])

        if case1 > case2:
            return i+1, j, nums1[i]
        else:
            return i, j+1, nums2[j]


print Solution().largestNumber([3, 30, 34, 5, 9])
print Solution().largestNumber([12, 121])
print Solution().largestNumber([0,0])
