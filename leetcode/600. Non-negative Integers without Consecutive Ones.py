import numpy as np
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
        """


        # dp1[i] is number binary string with length i with no consecutive 1 end in 0
        # dp2[i] is number binary string with length i with no consecutive 1 end in 1
        A = bin(num)[::-1]
        m = len(A)-2
        dp1 = [0] * m
        dp2 = [0] * m
        dp1[0] = 1
        dp2[0] = 1

        s = 1 if A[0] == '0' else 2
        for i in range(1, m):
            dp1[i] = dp1[i-1] + dp2[i-1]
            dp2[i] = dp1[i-1]

            # s = dp1[m-2] + dp2[m-2] # number of binary with length m with no consecutive 1
            if A[i-1:i+1]=='01':
                # if A[i-1:i+1]=='01', we can append '1' after integers less than A[:i] without consecutive ones,
                # also any integer with (i+1) bits, highest bit is '0', without consecutive ones
                # is less than A[:i+1]
                s+=dp1[i]
            elif A[i-1:i+1]=='11':
                # if A[i-1:i+1]=='11', then any integer with i+1 bits and without consecutive ones
                # is less than A[:i+1]
                s=dp1[i]+dp2[i]
                # if A[i]=='0', the number of integers  with i+1 bits, less than A[:i+1]  and without
                # consecutive ones is the same as A[:i]


        return s


    def print_binary(self, n):
        for j in range(n+1):
            print bin(j)



num = 5
Solution().print_binary(num)
print Solution().findIntegers(num)