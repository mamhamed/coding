class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if len(edges) == 0:
            return 0

        parents = {}
        for e in edges:
            parents[e[0]] = e[0]
            parents[e[1]] = e[1]

        for e in edges:
            if self.find(parents, e[0]) == self.find(parents, e[1]):
                return e
            else:
                parents[self.find(parents, e[0])] = self.find(parents, e[1])

    def find(self, parents, node):
        if parents[node] != node:
            parents[node] = self.find(parents, parents[node])

        return parents[node]



print Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])  # [1, 4]
print Solution().findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]])  # [2,5]