"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""
class DfsSolution(object):
    def is_valid_tree(self, n, edges):
        nodes = range(n)

        # if len(edges) >= n:
        #     return False

        ed = {}
        for e in edges:
            ed[e[0]] = ed.get(e[0], []) + [e[1]]
            ed[e[1]] = ed.get(e[1], []) + [e[0]]

        visited = {}
        a = self.dfs(ed, 0, visited)
        if len(visited) != n or not a:
            return False

        return True

    def dfs(self, edges, current_node, visited, par=-1):
        e = edges[current_node]
        visited[current_node] = True
        for child in e:
            if child != par:
                if child in visited.keys():
                    return False
                if not self.dfs(edges, child, visited, current_node):
                    return False

        return True


class BfsSolution(object):
    def is_valid_tree(self, n, edges):
        nodes = range(n)

        ed = {}
        for e in edges:
            for j in {0, 1}:
                if e[j] in ed:
                    ed[e[j]].add(e[1-j])
                else:
                    ed[e[j]] = set([e[1-j]])

        queue = [nodes[0]]
        visited = []

        while len(queue) > 0:
            node = queue.pop()
            if node in visited:
                return False
            connected_nodes = ed[node]
            for n in connected_nodes:
                ed[n].remove(node)

        return visited == n




# print DfsSolution().is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
# print DfsSolution().is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])

print BfsSolution().is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print BfsSolution().is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])