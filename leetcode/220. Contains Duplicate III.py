class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int  # difference between values
        :rtype: bool
        """
        if nums is None or len(nums) <= 1:
            return False
        if t < 0:
            return False

        buckets = {}
        w = t + 1 # bucketize
        for i, v in enumerate(nums):
            bucketNum = v / w
            r = {-1,0,1}
            rr = []
            for idx in r:
                if bucketNum+idx in buckets:
                    rr.append(idx)
            for idx in rr:
                for c, d in buckets[bucketNum+idx]:
                    if abs(i-c) <= k and abs(d-v) <= t:
                        return True

            buckets[bucketNum] = buckets.get(bucketNum, []) + [(i,v)]

        return False


print Solution().containsNearbyAlmostDuplicate([2,3,1,9,7,6], 1, 1)