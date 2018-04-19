class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """

        n = len(ring)
        m = len(key)
        mat = [[0]*n for _ in range(m)]

        for i,v in enumerate(key):
            if i == 0:
                costs = self.calculate_cost(ring, 0, v)
                for j,k in costs.items():
                    mat[i][j] = k
            else:
                prev = mat[i-1]
                for idx, val in enumerate(prev):
                    if val != 0:
                        costs = self.calculate_cost(ring, idx, v)
                        for j, k in costs.items():
                            if mat[i][j] == 0:
                                mat[i][j] = k + val
                            else:
                                mat[i][j] = min(k + val, mat[i][j])

        min_val = n*len(key)
        for i in mat[-1]:
            if i > 0 and i < min_val:
                min_val = i

        return min_val

    def calculate_cost(self, ring, index, s):
        costs = {}
        for i,v in enumerate(ring):
            if v == s:
                costs[i] = min(abs(index - i), abs(len(ring)-index+i), abs(len(ring)+index-i))+1
        return costs

print Solution().findRotateSteps("godding", 'gd')
print Solution().findRotateSteps("abcde", 'ade')
print Solution().findRotateSteps("pqwcx", "cpqwx")