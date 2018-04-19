#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self, v, visited):
        if v in visited:
            return
        print v
        visited[v] = True

        for u in self.graph[v]:
            if u not in visited:
                self.dfs(u, visited)

        return

    def dfs_main(self):
        visited = {}
        for v in range(self.V-1, -1, -1):
            if v not in visited:
                self.dfs(v, visited)


    def topologicalSortingUtils(self, v, stack, visited):
        if v in visited:
            return
        visited[v] = True

        for u in self.graph[v]:
            if u not in visited:
                self.topologicalSortingUtils(u, stack, visited)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = {}
        stack = []
        for v in range(self.V-1, -1, -1):
            if v not in visited:
                self.topologicalSortingUtils(v, stack, visited)

        print stack




g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print "Following is dfs"
g.dfs_main()

print "Following is a Topological Sort of the given graph"
g.topologicalSort()
