

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0

        envelopes_with_area = [(x, x[0]*x[1]) for x in envelopes]
        envelopes_with_area = sorted(envelopes_with_area, key=lambda x:x[1])
        envelopes_sorted = [x[0] for x in envelopes_with_area]
        max_env_hold_at_i = [1] * len(envelopes_sorted)
        for i in range(len(envelopes_sorted)):
            for j in range(i):
                if self.is_fit(envelopes_sorted[j], envelopes_sorted[i]):
                    max_env_hold_at_i[i] = max(max_env_hold_at_i[i], max_env_hold_at_i[j]+1)

        return max(max_env_hold_at_i)



    def is_fit(self, child_env, parent_env):
        if child_env[0] < parent_env[0] and child_env[1] < parent_env[1]:
            return True

        return False






print Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])