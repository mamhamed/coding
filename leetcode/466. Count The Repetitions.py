class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        cnt = 0
        cnt2 = 0
        i = 0
        j = 0
        while cnt2 < n1:
            if s1[j] == s2[i]:
                i += 1
                j += 1
            else:
                j += 1

            if i == len(s2):
                i = 0
                cnt += 1

            if j == len(s1):
                j = 0
                cnt2 += 1

        return cnt/n2


print Solution().getMaxRepetitions(s1="acb", n1=4, s2="ab", n2=2)

print Solution().getMaxRepetitions(s1="acb", n1=4, s2="abc", n2=2)

print Solution().getMaxRepetitions(s1="aaa", n1=3, s2="aa", n2=1)
