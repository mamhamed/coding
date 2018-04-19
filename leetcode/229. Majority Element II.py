import sys
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        cnt1, cnt2, cand1, cand2 = 0, 0, 0, 0
        for x in nums:
            if cnt1 == 0 and x != cand2:
                cand1 = x
                cnt1 = 1
            elif x == cand1:
                cnt1 += 1
            else:
                if cnt2 == 0:
                    cand2 = x
                    cnt2 = 1
                elif x == cand2:
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1

        i, j = 0, 0
        for x in nums:
            if x == cand1:
                i += 1
            elif x == cand2:
                j += 1

        res = []
        if i > n/3:
            res.append(cand1)
        if j > n/3:
            res.append(cand2)
        return res




# print Solution().majorityElement([])
# print Solution().majorityElement([0,3,4,0])
# print Solution().majorityElement([1,2])
# print Solution().majorityElement([1])
# print Solution().majorityElement([1,1,1,3])
# print Solution().majorityElement([1,1,1,2,2,4])
# print Solution().majorityElement([1,2,3])
# print Solution().majorityElement([1,1,1])
# print Solution().majorityElement([1,3,3])
print Solution().majorityElement([1,2,2,3,2,1,1,3])