class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # cnt = 0
        # start = 0
        # while start < n:
        #     if s[start] == '0':
        #         i = start
        #         while i < n and s[i] == '0':
        #             i += 1
        #         zero_end = i
        #         len_zero = i - start
        #         len_one = 0
        #         while i < n and s[i] == '1':
        #             len_one += 1
        #             i += 1
        #
        #         cnt += min(len_zero, len_one)
        #         start = zero_end
        #     else:
        #         i = start
        #         while i < n and s[i] == '1':
        #             i += 1
        #         one_end = i
        #         len_one = i - start
        #         len_zero = 0
        #         while i < n and s[i] == '0':
        #             len_zero += 1
        #             i += 1
        #
        #         cnt += min(len_zero, len_one)
        #         start = one_end
        #
        # return cnt
        n = len(s)
        cnt = 0
        i = 0
        while i < n-1:
            if s[i:i+2] == "01":
                cnt += 1
                j = 1
                while i-j >=0 and i+1+j <n and s[i-j] == '0' and s[i+1+j] == '1':
                    j += 1
                    cnt += 1
                i = i+j
            elif s[i:i+2] == "10":
                cnt += 1
                j = 1
                while i-j >=0 and i+1+j <n and s[i-j] == '1' and s[i+1+j] == '0':
                    j += 1
                    cnt += 1
                i = i+j
            else:
                i += 1

        return cnt

print Solution().countBinarySubstrings("00110")  # 3
print Solution().countBinarySubstrings("00110011")  # 6
print Solution().countBinarySubstrings("10101")  # 4