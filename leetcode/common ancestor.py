

def find_common_ancestor(connections, n1, n2):

    parents = {}

    for e in connections:
        parents[e[1]] = parents.get(e[1], []) + [e[0]]
        if e[0] not in parents:
            parents[e[0]] = [e[0]]

    parents1 = set([])
    parents2 = set([])
    get_all_parents(parents, n1, parents1)
    get_all_parents(parents, n2, parents2)

    for v in parents1:
        if v in parents2:
            return v

def get_parent(parents, node):
    if parents[node] == node:
        return node
    else:
        return get_parent(parents, parents[node])

def get_all_parents(parents, node, arr):
    if parents[node] == node:
        arr.add(node)
        return node
    else:
        arr.add(node)
        get_all_parents(parents, parents[node], arr)


print find_common_ancestor([[1,2], [1,3], [3,4], [5,4], [2,6]], 4, 6)