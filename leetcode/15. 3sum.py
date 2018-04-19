## 2nd attempt
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         if n < 3:
#             return []
#         sorted_nums = sorted(nums)
#
#         res = []
#         dic = {}
#         i = 0
#
#         while i < n-1:
#             if sorted_nums[i] == sorted_nums[i+1]:
#                 i += 1
#                 continue
#             else:
#                 j = i+1
#                 while j < n:
#                     if sorted_nums[j-1] == sorted_nums[j]:
#                         j += 1
#                         continue
#                     else:
#                         if -sorted_nums[j] in dic:
#                             for x in dic[-sorted_nums[j]]:
#                                 res.append(x+[sorted_nums[j]])
#                         else:
#                             s = sorted_nums[i] + sorted_nums[j]
#                             dic[s] = dic.get(s, []) + [[sorted_nums[i], sorted_nums[j]]]
#                         j +=1
#                 i += 1
#
#         return res



## first attempt
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         if n < 3:
#             return []
#
#         nums = sorted(nums)
#         all_sums = []
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             ptr1 = i + 1
#             ptr2 = n-1
#             target = -nums[i]
#             while ptr1 < n and ptr1 < ptr2:
#                 d = nums[ptr1] + nums[ptr2]
#                 if target == d:
#                     all_sums.append([nums[i], nums[ptr1], nums[ptr2]])
#                     while ptr1 < n-1 and nums[ptr1] == nums[ptr1+1]:
#                         ptr1 += 1
#                     ptr1 += 1
#                     while ptr2 >= 0 and nums[ptr2] == nums[ptr2-1]:
#                         ptr2 -= 1
#                     ptr2 -= 1
#                 elif target < d:
#                     ptr2 -= 1
#                 else:
#                     ptr1 += 1
#
#         return all_sums


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
print Solution().threeSum([0,0,2,0])
print Solution().threeSum([0,0,0,0])
print Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
print Solution().threeSum([1,1,-2])
print Solution().threeSum([-1,0,1,2,-1,-4])