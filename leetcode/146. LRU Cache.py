import sys
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.pointer = {}
        self.head = Node(-sys.maxint)
        self.tail = Node(sys.maxint)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1

        node = self.pointer[key]
        self.remove_node(node)
        self.add_to_end(node)
        return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        if key in self.dic:
            self.dic[key] = value
            self.get(key)
            return

        if len(self.dic) >= self.capacity:
            # remove
            node = self.head.next
            self.pointer.pop(node.val, None)
            self.dic.pop(node.val, None)
            self.remove_node(node)

        self.dic[key] = value
        node = Node(key)
        self.pointer[key] = node
        self.add_to_end(node)

        return

    def remove_node(self, node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a

    def add_to_end(self, node):
        tmp = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev = tmp
        tmp.next = node


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

def run(ops, data):
    cls = LRUCache(data[0][0])
    i = 1
    for op in ops[1:]:
        d = data[i]
        if op == "put":
            cls.put(d[0],d[1])
        if op == "get":
            print cls.get(d[0])

        i += 1

# run(["LRUCache","put","put","get","put","get","put","get","get","get"],
#     [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])

run(["LRUCache","put","get","put","get","get"],
    [[1],[2,1],[2],[3,2],[2],[3]])