"""
in an stream of unique numbers, keep the top k largest one
think of stream of numbers as link list
for simplicity we implement in arr
"""

import bisect
import heapq
class Solution(object):
    def top_k(self, nums, k):
        arr = [nums[0]]
        heapq.heapify(arr)
        for num in nums[1:]:
            if num >= arr[0]:
                heapq.heappush(arr, num)
                if len(arr) > k:
                    heapq.heappop(arr)

        return arr


# import bisect
# class Solution(object):
#     def top_k(self, nums, k):
#         arr = [nums[0]]
#         for num in nums[1:]:
#             if num >= arr[0]:
#                 j = bisect.bisect_left(arr, num)
#                 arr.insert(j, num)
#                 if len(arr) > k:
#                     arr.pop(0)
#
#         return arr


print Solution().top_k([1,2,3,4,5,6,7,8,9], 3)