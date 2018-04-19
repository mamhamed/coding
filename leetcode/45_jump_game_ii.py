

# """
# This solution is based on recursion which implements DFS with memorization
# it finds correct solution but it can hit max recursion for a very long array
# """
# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         self.num_jumps_at_i = [0] * len(nums)
#         return self.jump_from_index(nums, 0)
#
#     def jump_from_index(self, nums, index):
#         if index >= len(nums):
#             return 0
#
#         if self.num_jumps_at_i[index] > 0:
#             return self.num_jumps_at_i[index]
#
#         jumps = []
#         for i in range(1,nums[index]+1):
#             if i+index < len(nums):
#                 jumps.append(self.jump_from_index(nums, index+i))
#             else:
#                 break
#
#         if len(jumps) > 0:
#             self.num_jumps_at_i[index] = min(jumps) + 1
#         else:
#             self.num_jumps_at_i[index] = 0
#
#         return self.num_jumps_at_i[index]

# dynamic programing approach with ON(N^2)
# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         min_jumps = [len(nums)] * len(nums)
#         min_jumps[0] = 0
#
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j]+j >= i:
#                     min_jumps[i] = min(min_jumps[j]+1, min_jumps[i])
#
#         return min_jumps[-1]


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        step = 0
        furthest = 0
        start = 0
        end = 0
        for i in range(len(nums)):
            step += 1
            for j in range(start, end+1):
                furthest = max(furthest, j+nums[j])
                if furthest >= len(nums)-1:
                    return step

            start = end + 1
            end = furthest

        return step

print Solution().jump([])
print Solution().jump([0])
print Solution().jump([1,2])
print Solution().jump([1,2,1,1,1])
print Solution().jump([2,3,1,1,4])
print Solution().jump([1,1,2,1,1])