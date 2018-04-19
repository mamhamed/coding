import numpy as np
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        n = len(s)

        mat = np.zeros([n,n])
        dp = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 2 or mat[i-1][j+1] == 1):
                    mat[i][j] = 1
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)

        return int(dp[n-1])

    def is_palindrome(self, s):
        n = len(s)
        if n <= 1:
            True

        return s == s[::-1]



print Solution().minCut("ab")  # a b
print Solution().minCut("aab")  # aa b
print Solution().minCut("hhabccb")  # hh a bccb
print Solution().minCut("hhabccbadfg") # hh abccba d f g
print Solution().minCut("hhdabccbadfg") # h dabccbad f g

# 452
# print Solution().minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")