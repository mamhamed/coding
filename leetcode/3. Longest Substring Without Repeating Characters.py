## this is second attempt
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        n = len(s)

        f = [0] * n  # f[i] largest substring including ith character
        last = 0
        dic = {}
        for i in range(n):
            c = s[i]
            if c not in dic or dic[c] < last:
                f[i] = f[i-1] + 1
            else:
                last = dic[c]
                f[i] = i-last

            dic[c] = i

        return max(f)


## this is first attempt
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0:
#             return 0
#
#         if len(s) == 1:
#             return 1
#
#         n = len(s)
#         f = [0] * n
#
#         dic = {}
#         start = 0
#         for i, char in enumerate(s):
#             if char not in dic:
#                 f[i] = f[i-1] + 1
#             else:
#                 if start <= dic[char]:
#                     f[i] = i - dic[char]
#                 else:
#                     f[i] = f[i-1] + 1
#                 start = max(dic[char] + 1, start)
#
#             dic[char] = i
#
#         return max(f)


print Solution().lengthOfLongestSubstring("abcabcbb")  # 3

print Solution().lengthOfLongestSubstring("pwwkew")  # 3

print Solution().lengthOfLongestSubstring("c")  # 1

print Solution().lengthOfLongestSubstring("ca")  # 2

print Solution().lengthOfLongestSubstring("cc")  # 1

print Solution().lengthOfLongestSubstring("tmmzuxt")  # 5

print Solution().lengthOfLongestSubstring("bpfbhmipx")  # 7

print Solution().lengthOfLongestSubstring("blqsearxxxbiwqa")  # 8