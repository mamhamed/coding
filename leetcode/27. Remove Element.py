class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)

        j = 0
        start = 0
        while j < n:
            if nums[j] == val:
                i = j+1
                while i < n and nums[i] == val:
                    i += 1
                if i < n:
                    nums[start], nums[i] = nums[i], nums[start]
                    start += 1
                j = i

            else:
                j += 1
                start += 1

        return start


nums = [3,2,2,3]
a = Solution().removeElement(nums, 3)  # 2
print nums[:a]

nums = [2]
a = Solution().removeElement([2], 3)  # 1
print nums[:a]

nums = [3,3,3,3]
a = Solution().removeElement(nums, 3)  # 0
print nums[:a]

nums = [0,4,4,0,4,4,4,0,2]
a = Solution().removeElement(nums, 4)
print nums[:a]