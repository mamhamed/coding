class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        mid = len(nums)/2
        if nums[mid] == target:
            return True

        start = 0
        while nums[start] == nums[mid] and start < mid:
            start += 1

        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                return self.search(nums[:mid], target)
            else:
                return self.search(nums[mid+1:], target)
        else:
            if nums[mid] <= target <= nums[-1]:
                return self.search(nums[mid+1:], target)
            else:
                return self.search(nums[:mid], target)


print Solution().search([1,1,1,3,1], 3)
print Solution().search([1,3,1,1,1], 3)
print Solution().search([1], 0)