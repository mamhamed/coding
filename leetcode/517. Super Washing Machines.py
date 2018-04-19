class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        m = sum(machines)
        if m % n != 0:
            return -1

        avg_d = m/n
        move = [0] * n

        res = 0
        for i in range(n-1):
            v = machines[i]
            if v < avg_d:
                move[i+1] = avg_d - v
                machines[i+1] -= avg_d - v
                machines[i] = avg_d
                res = max(res, move[i+1])
            elif v > avg_d:
                move[i] += v - avg_d
                machines[i+1] += v - avg_d
                machines[i] = avg_d
                res = max(res, move[i])

        return res




# print Solution().findMinMoves([1,0,5])
print Solution().findMinMoves([0,3,0])
