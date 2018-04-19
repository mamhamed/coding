import numpy as np

class Solution():
    def longest_common_substring(self, s1, s2):
        n = len(s1)
        m = len(s2)

        mat = np.zeros(shape=(n,m))

        all_max = 0
        all_max_i = -1

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = mat[i-1][j-1] + 1
                if mat[i][j] > all_max:
                    all_max = mat[i][j]
                    all_max_i = i

        return all_max_i, all_max


print Solution().longest_common_substring("abb", "bba")

"abb"
"bba"