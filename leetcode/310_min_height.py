class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        node_map = {}
        for e in edges:
            node_map[e[0]] = node_map.get(e[0], []) + [e[1]]
            node_map[e[1]] = node_map.get(e[1], []) + [e[0]]

        best_level = n
        heads = []
        for i in range(n):
            visited = []
            level = 0
            queue = [i]
            flag = True
            while flag:
                next_queue = []
                while len(queue) > 0:
                    node = queue.pop(0)
                    visited.append(node)
                    nb = node_map[node]
                    nb = [x for x in nb if x not in visited]
                    next_queue += nb
                queue = [x for x in next_queue]
                level += 1
                if len(queue) == 0:
                    flag = False

            if level < best_level:
                best_level = level
                heads = [i]
            elif level == best_level:
                heads.append(i)

        return heads


print Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]])